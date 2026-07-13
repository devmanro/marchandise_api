# predict_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import joblib
import re
from collections import defaultdict

app = FastAPI(title="Marchandise Prediction API")

model = joblib.load("marchandise_model.pkl")
target_cols = ["Marchandise2", "Modèle", "Détails PRODUITS", "PRODUITS"]


# ─────────────────────────────────────────────────────────────────
# Schemas
# ─────────────────────────────────────────────────────────────────

class PredictRequest(BaseModel):
    marchandise: str
    nb_colis: Optional[int] = None
    poids_brut_total: Optional[float] = None


class VehicleUnit(BaseModel):
    """One classified vehicle/equipment line."""
    raw_segment: str
    quantity: int
    vehicle_type: str           # e.g. "CRAWLER EXCAVATOR", "WHEEL LOADER"
    Marchandise2: str
    Modele: str
    Details_PRODUITS: str
    PRODUITS: str
    poids_brut: Optional[float] = None
    nombre_colis: Optional[float] = None


class PackageGroup(BaseModel):
    """Grouped packages (non-unit items)."""
    descriptions: list[str]
    total_pkgs: int
    Marchandise2: str
    Modele: str
    Details_PRODUITS: str
    PRODUITS: str
    poids_brut: Optional[float] = None
    nombre_colis: Optional[float] = None


class GroupedByModel(BaseModel):
    """Aggregated view per Modèle."""
    Modele: str
    Marchandise2: str
    Details_PRODUITS: str
    PRODUITS: str
    vehicle_types: list[str]       # all vehicle types in this model group
    total_units: int
    total_pkgs: int
    poids_brut: Optional[float] = None
    nombre_colis: Optional[float] = None


class PredictResponse(BaseModel):
    original_marchandise: str
    total_units: int
    total_pkgs: int
    nb_colis: Optional[int]
    poids_brut_total: Optional[float]
    # Detailed per-vehicle breakdown
    vehicle_units: list[VehicleUnit]
    # Package summary
    packages: Optional[PackageGroup]
    # Aggregated by model
    grouped_by_model: list[GroupedByModel]


# ─────────────────────────────────────────────────────────────────
# Text helpers
# ─────────────────────────────────────────────────────────────────

def clean_text(text: str) -> str:
    text = str(text).upper()
    text = re.sub(r'[^A-Z0-9 ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# Matches "4 UNITS CRAWLER EXCAVATOR" or "1 UNIT MAINTENANCE PARTS"
UNIT_RE = re.compile(
    r'^(\d+)\s+UNITS?\s+(.+)',
    re.IGNORECASE
)

# Noise-only strings to discard
NOISE_RE = re.compile(
    r'^(PKGS?\.?|PACKAGES?\.?|N/?A|\.+|\-+)\s*$',
    re.IGNORECASE
)


def predict_single(text: str) -> dict:
    """Run model on a single text, returns dict of target_cols."""
    cleaned = clean_text(text)
    preds   = model.predict([cleaned])[0]
    return dict(zip(target_cols, preds))


def is_unknown(val: str) -> bool:
    return str(val).strip().upper() in ("", "UNKNOWN", "N/A", "AUTRES")


def resolve_vehicle_type(description: str, pred: dict) -> str:
    """
    Pick the best human-readable vehicle type name:
      Priority: Détails PRODUITS → Marchandise2 → raw description
    """
    details = pred.get("Détails PRODUITS", "")
    marc2   = pred.get("Marchandise2", "")

    if not is_unknown(details):
        return details.upper()
    if not is_unknown(marc2):
        return marc2.upper()
    # Fall back to the raw parsed description (cleaned up)
    return description.upper().strip()


def distribute(total: Optional[float], quantities: list[int]) -> list[Optional[float]]:
    """Proportional distribution of a total across quantities."""
    if total is None or sum(quantities) == 0:
        return [None] * len(quantities)
    grand = sum(quantities)
    return [round(total * q / grand, 4) for q in quantities]


# ─────────────────────────────────────────────────────────────────
# Main parser
# ─────────────────────────────────────────────────────────────────

def parse_and_classify(
    marchandise: str,
    nb_colis: Optional[int],
    poids_brut_total: Optional[float],
) -> dict:
    """
    Full pipeline:
      1. Split by '/' → slash blocks
      2. Within each block split by '+' → parts
      3. Classify each part as UNIT or PKG
      4. Predict each segment independently
      5. Resolve vehicle type from prediction
      6. Distribute weight & colis proportionally
      7. Group by Modèle
    """

    # ── 1 & 2 : split into individual parts ─────────────────────────────────
    unit_entries = []    # list of {quantity, description, raw}
    pkg_descs    = []    # list of raw strings that are packages

    slash_blocks = [b.strip() for b in marchandise.split('/') if b.strip()]

    for block in slash_blocks:
        plus_parts = [p.strip() for p in block.split('+') if p.strip()]
        for part in plus_parts:
            m = UNIT_RE.match(part.strip())
            if m:
                qty  = int(m.group(1))
                desc = m.group(2).strip()
                unit_entries.append({
                    "quantity"   : qty,
                    "description": desc,
                    "raw"        : part.strip(),
                })
            else:
                if not NOISE_RE.match(part.strip()) and part.strip():
                    pkg_descs.append(part.strip())

    # ── 3 : compute unit / pkg totals ────────────────────────────────────────
    total_units = sum(e["quantity"] for e in unit_entries)
    total_pkgs  = max(0, (nb_colis or 0) - total_units)

    # ── 4 : predict each UNIT segment ────────────────────────────────────────
    # quantities list for weight distribution (units first, then pkg block)
    all_quantities = [e["quantity"] for e in unit_entries] + [total_pkgs]
    poids_shares   = distribute(poids_brut_total, all_quantities)
    colis_shares   = distribute(
        float(nb_colis) if nb_colis else None, all_quantities
    )

    vehicle_units: list[VehicleUnit] = []

    for i, entry in enumerate(unit_entries):
        pred = predict_single(entry["description"])
        vtype = resolve_vehicle_type(entry["description"], pred)

        vehicle_units.append(VehicleUnit(
            raw_segment      = entry["raw"],
            quantity         = entry["quantity"],
            vehicle_type     = vtype,
            Marchandise2     = pred["Marchandise2"],
            Modele           = pred["Modèle"],
            Details_PRODUITS = pred["Détails PRODUITS"],
            PRODUITS         = pred["PRODUITS"],
            poids_brut       = poids_shares[i],
            nombre_colis     = colis_shares[i],
        ))

    # ── 5 : classify packages (use combined description for prediction) ───────
    pkg_block: Optional[PackageGroup] = None
    if total_pkgs > 0 or pkg_descs:
        combined_pkg_text = " ".join(pkg_descs) if pkg_descs else "PACKAGES"
        pkg_pred = predict_single(combined_pkg_text)
        pkg_block = PackageGroup(
            descriptions     = pkg_descs,
            total_pkgs       = total_pkgs,
            Marchandise2     = pkg_pred["Marchandise2"],
            Modele           = pkg_pred["Modèle"],
            Details_PRODUITS = pkg_pred["Détails PRODUITS"],
            PRODUITS         = pkg_pred["PRODUITS"],
            poids_brut       = poids_shares[-1],   # last share = pkg block
            nombre_colis     = colis_shares[-1],
        )

    # ── 6 : group by Modèle ──────────────────────────────────────────────────
    groups: dict[str, dict] = {}

    def _add_to_group(
        modele: str, marc2: str, details: str, produits: str,
        vtype: str, qty_units: int, qty_pkgs: int,
        poids: Optional[float], colis: Optional[float],
    ):
        if modele not in groups:
            groups[modele] = {
                "Modele"          : modele,
                "Marchandise2"    : marc2,
                "Details_PRODUITS": details,
                "PRODUITS"        : produits,
                "vehicle_types"   : [],
                "total_units"     : 0,
                "total_pkgs"      : 0,
                "poids_brut"      : 0.0 if poids is not None else None,
                "nombre_colis"    : 0.0 if colis is not None else None,
            }
        g = groups[modele]
        if vtype and vtype not in g["vehicle_types"]:
            g["vehicle_types"].append(vtype)
        g["total_units"] += qty_units
        g["total_pkgs"]  += qty_pkgs
        if poids is not None:
            g["poids_brut"]   = round((g["poids_brut"]   or 0) + poids, 4)
        if colis is not None:
            g["nombre_colis"] = round((g["nombre_colis"] or 0) + colis, 4)

    for v in vehicle_units:
        _add_to_group(
            v.Modele, v.Marchandise2, v.Details_PRODUITS, v.PRODUITS,
            v.vehicle_type, v.quantity, 0,
            v.poids_brut, v.nombre_colis,
        )

    if pkg_block:
        _add_to_group(
            pkg_block.Modele, pkg_block.Marchandise2,
            pkg_block.Details_PRODUITS, pkg_block.PRODUITS,
            "",                          # no vehicle type for pkgs
            0, pkg_block.total_pkgs,
            pkg_block.poids_brut, pkg_block.nombre_colis,
        )

    return {
        "total_units"     : total_units,
        "total_pkgs"      : total_pkgs,
        "vehicle_units"   : vehicle_units,
        "packages"        : pkg_block,
        "grouped_by_model": [GroupedByModel(**g) for g in groups.values()],
    }


# ─────────────────────────────────────────────────────────────────
# Endpoint
# ─────────────────────────────────────────────────────────────────
@app.get("/")
def root():
    return {"status": "ok", "message": "Marchandise API is running"}
  
@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    if not req.marchandise.strip():
        raise HTTPException(status_code=400, detail="marchandise is empty")

    result = parse_and_classify(
        req.marchandise,
        req.nb_colis,
        req.poids_brut_total,
    )

    return PredictResponse(
        original_marchandise = req.marchandise,
        nb_colis             = req.nb_colis,
        poids_brut_total     = req.poids_brut_total,
        **result,
    )


@app.get("/health")
def health():
    return {"status": "ok"}
