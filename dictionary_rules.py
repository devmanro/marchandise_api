import re

def normalize(text):
    text = str(text).upper()
    text = re.sub(r'[^A-Z0-9 ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


RULES = {
    # ─── COLIS / GENERIC ───────────────────────────────────────────────
    "STEEL FORMWORK": {
        "Marchandise2": "COLIS",
        "Modele": "COLIS",
        "Détails PRODUITS": "COLIS",
        "PRODUITS": "COLIS"
    },
    "GANTRY CRANE": {
        "Marchandise2": "COLIS",
        "Modele": "COLIS",
        "Détails PRODUITS": "COLIS",
        "PRODUITS": "COLIS"
    },
    "SLAG POT": {
        "Marchandise2": "COLIS",
        "Modele": "COLIS",
        "Détails PRODUITS": "COLIS",
        "PRODUITS": "COLIS"
    },
    "TISSUE MACHINE": {
        "Marchandise2": "COLIS",
        "Modele": "COLIS",
        "Détails PRODUITS": "COLIS",
        "PRODUITS": "COLIS"
    },
    "SPARE PARTS FOR BUS": {
        "Marchandise2": "COLIS",
        "Modele": "COLIS",
        "Détails PRODUITS": "COLIS",
        "PRODUITS": "COLIS"
    },

    # ─── STEEL / METALS ────────────────────────────────────────────────
    "DRILL PIPE": {
        "Marchandise2": "TUBES",
        "Modele": "TUBES",
        "Détails PRODUITS": "TUBES",
        "PRODUITS": "TUBES"
    },
    "H-BEAM": {
        "Marchandise2": "POUTRELLES",
        "Modele": "POUTRELLES",
        "Détails PRODUITS": "POUTRELLES",
        "PRODUITS": "POUTRELLES"
    },
    "I-BEAM": {
        "Marchandise2": "POUTRELLES",
        "Modele": "POUTRELLES",
        "Détails PRODUITS": "POUTRELLES",
        "PRODUITS": "POUTRELLES"
    },
    "U PROFILE": {
        "Marchandise2": "POUTRELLES",
        "Modele": "POUTRELLES",
        "Détails PRODUITS": "POUTRELLES",
        "PRODUITS": "POUTRELLES"
    },
    "U-PROFILE": {
        "Marchandise2": "POUTRELLES",
        "Modele": "POUTRELLES",
        "Détails PRODUITS": "POUTRELLES",
        "PRODUITS": "POUTRELLES"
    },
    "CHANNEL": {
        "Marchandise2": "POUTRELLES",
        "Modele": "POUTRELLES",
        "Détails PRODUITS": "POUTRELLES",
        "PRODUITS": "POUTRELLES"
    },
    "ANGLE BAR": {
        "Marchandise2": "CORNIERES",
        "Modele": "CORNIERES",
        "Détails PRODUITS": "CORNIERES",
        "PRODUITS": "CORNIERES"
    },
    "TINNED": {
        "Marchandise2": "BOBINES",
        "Modele": "BOBINES",
        "Détails PRODUITS": "BOBINES",
        "PRODUITS": "BOBINES"
    },
    "PRE-PAINTED STEEL IN COILS": {
        "Marchandise2": "BOBINES",
        "Modele": "BOBINES",
        "Détails PRODUITS": "BOBINES",
        "PRODUITS": "BOBINES"
    },
    "COLD ROLLED STEEL IN COILS": {
        "Marchandise2": "BOBINES",
        "Modele": "BOBINES",
        "Détails PRODUITS": "BOBINES",
        "PRODUITS": "BOBINES"
    },
    "HOT ROLLED STEEL IN COILS": {
        "Marchandise2": "BOBINES",
        "Modele": "BOBINES",
        "Détails PRODUITS": "BOBINES",
        "PRODUITS": "BOBINES"
    },
    "HOT ROLLED COIL": {
        "Marchandise2": "BOBINES",
        "Modele": "BOBINES",
        "Détails PRODUITS": "BOBINES",
        "PRODUITS": "BOBINES"
    },
    "HOT ROLLED STEEL COIL": {
        "Marchandise2": "BOBINES",
        "Modele": "BOBINES",
        "Détails PRODUITS": "BOBINES",
        "PRODUITS": "BOBINES"
    },

    # ─── WOOD / PANEL PRODUCTS ─────────────────────────────────────────
    "PLAIN MDF": {
        "Marchandise2": "CTP",
        "Modele": "CTP",
        "Détails PRODUITS": "CTP",
        "PRODUITS": "CTP"
    },
    "FANCY MDF": {
        "Marchandise2": "CTP",
        "Modele": "CTP",
        "Détails PRODUITS": "MDF",
        "PRODUITS": "CTP"
    },
    "FILM FACED PLYWOOD": {
        "Marchandise2": "CTP",
        "Modele": "CTP",
        "Détails PRODUITS": "FFP",
        "PRODUITS": "CTP"
    },
    "BLOCKBOARD": {
        "Marchandise2": "CTP",
        "Modele": "CTP",
        "Détails PRODUITS": "MDF",
        "PRODUITS": "CTP"
    },
    "COMMERCIAL PLYWOOD": {
        "Marchandise2": "CTP",
        "Modele": "CTP",
        "Détails PRODUITS": "MDF + PLYWOOD",
        "PRODUITS": "CTP"
    },
    "MDF": {
        "Marchandise2": "CTP",
        "Modele": "CTP",
        "Détails PRODUITS": "MDF",
        "PRODUITS": "CTP"
    },

    # ─── BUSES ─────────────────────────────────────────────────────────
    "AUTOBUS": {
        "Marchandise2": "AUTOBUS",
        "Modele": "C-100-KLQ6106G",
        "Détails PRODUITS": "BUS",
        "PRODUITS": "UTILITAIRE"
    },
    "AUTOCAR": {
        "Marchandise2": "AUTOCAR",
        "Modele": "V-11-KLQ6116",
        "Détails PRODUITS": "BUS",
        "PRODUITS": "UTILITAIRE"
    },
    "HIGER AUTOBUS": {
        "Marchandise2": "AUTOBUS",
        "Modele": "C-100-KLQ6106G",
        "Détails PRODUITS": "BUS",
        "PRODUITS": "UTILITAIRE"
    },
    "HIGER AUTOCAR": {
        "Marchandise2": "AUTOCAR",
        "Modele": "V-11-KLQ6116",
        "Détails PRODUITS": "BUS",
        "PRODUITS": "UTILITAIRE"
    },
    "MICRO BUS": {
        "Marchandise2": "MICRO BUS",
        "Modele": "KLQ6541C",
        "Détails PRODUITS": "MINI BUS",
        "PRODUITS": "UTILITAIRE"
    },

    # ─── DUMP TRUCKS ───────────────────────────────────────────────────
    "DUMP TRUCK": {
        "Marchandise2": "DUMP TRUCK",
        "Modele": "SX3255JM384",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "MINI DUMP TRUCK": {
        "Marchandise2": "MINI DUMP TRUCK",
        "Modele": "4*2 MINI DUMP TRUCK",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "TIPPER TRUCK": {
        "Marchandise2": "TIPPER TRUCK",
        "Modele": "ZZ3257N384GB1",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "TIPPER-AUTOMATIC": {
        "Marchandise2": "TIPPER-AUTOMATIC",
        "Modele": "SITRAK",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },

    # ─── MIXER / PUMP / CONCRETE TRUCKS ────────────────────────────────
    "MIXER TRUCK": {
        "Marchandise2": "MIXER TRUCK",
        "Modele": "10JBH",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "PUMP TRUCK": {
        "Marchandise2": "PUMP TRUCK",
        "Modele": "38X-5RZ",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "CONCRETE MIXER TRUCK": {
        "Marchandise2": "CONCRETE MIXER TRUCK",
        "Modele": "SX5255GJBJR334",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "CONCRETE MIXER": {
        "Marchandise2": "CONCRETE MIXER",
        "Modele": "HY-3500",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "CONCRETE PUMP TRUCK": {
        "Marchandise2": "CONCRETE PUMP TRUCK",
        "Modele": "ZLJ5291THBKF",
        "Détails PRODUITS": "CAMION POMPE A BETON",
        "PRODUITS": "LOURD"
    },
    "CONCRETE TRUCK MIXER": {
        "Marchandise2": "CONCRETE TRUCK MIXER",
        "Modele": "10JBH",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "SPRINKLER TRUCK": {
        "Marchandise2": "SPRINKLER TRUCK",
        "Modele": "SX5255GYSDN434",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "WATER TRUCK": {
        "Marchandise2": "WATER TRUCK",
        "Modele": "SX5255GYSJM434",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "WATER TANKER TRUCK": {
        "Marchandise2": "WATER TANKER TRUCK",
        "Modele": "SX5255GYSJM434",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "WATER TANK TRUCK": {
        "Marchandise2": "WATER TANK TRUCK",
        "Modele": "SX5255GSSJM434",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "GARBAGE TRUCK": {
        "Marchandise2": "GARBAGE TRUCK",
        "Modele": "PGC480L-II",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },

    # ─── CARGO / FREIGHT / LORRY TRUCKS ────────────────────────────────
    "FREIGHT TRUCK": {
        "Marchandise2": "FREIGHT TRUCK",
        "Modele": "NJ5046XXY4A",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "LORRY TRUCK": {
        "Marchandise2": "LORRY TRUCK",
        "Modele": "SX11858J501",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "CARGO TRUCK": {
        "Marchandise2": "CARGO TRUCK",
        "Modele": "SX11858J501",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "MINI CARGO TRUCK": {
        "Marchandise2": "MINI CARGO TRUCK",
        "Modele": "AUTRES",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "CHASSIS TRUCK": {
        "Marchandise2": "CHASSIS TRUCK",
        "Modele": "SX11858J501",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "AERIAL WORK TRUCK": {
        "Marchandise2": "AERIAL WORK TRUCK",
        "Modele": "SCS5045JGKJX6",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "ASPHALT DISTRIBUTOR": {
        "Marchandise2": "ASPHALT DISTRIBUTOR",
        "Modele": "XLS705A",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "CAMION": {
        "Marchandise2": "CAMION",
        "Modele": "ZZ3316V306MC1",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },

    # ─── TRACTORS ──────────────────────────────────────────────────────
    "TRACTOR TRUCK": {
        "Marchandise2": "TRACTOR TRUCK",
        "Modele": "ZZ4256V364HC1B",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "TRACTOR": {
        "Marchandise2": "TRACTOR",
        "Modele": "ZZ4256V364HC1B",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },

    # ─── SEMI-TRAILERS / TRAILERS ───────────────────────────────────────
    "SEMI-TRAILER": {
        "Marchandise2": "SEMI-TRAILER",
        "Modele": "70 TONS TRI-AXLE LOWBED SEMI-TRAILER",
        "Détails PRODUITS": "REMORQUES",
        "PRODUITS": "LOURD"
    },
    "SEMI TRAILER": {
        "Marchandise2": "SEMI TRAILER",
        "Modele": "CSQ9401D",
        "Détails PRODUITS": "REMORQUES",
        "PRODUITS": "LOURD"
    },
    "TRAILER": {
        "Marchandise2": "TRAILER",
        "Modele": "WTY94006P640",
        "Détails PRODUITS": "REMORQUES",
        "PRODUITS": "LOURD"
    },

    # ─── EXCAVATORS ────────────────────────────────────────────────────
    "EXCAVATOR": {
        "Marchandise2": "EXCAVATOR",
        "Modele": "HX340HD",
        "Détails PRODUITS": "EXCAVATEURS",
        "PRODUITS": "ENGINS"
    },
    "CRAWLER EXCAVATOR": {
        "Marchandise2": "CRAWLER EXCAVATOR",
        "Modele": "HX340HD",
        "Détails PRODUITS": "EXCAVATEURS",
        "PRODUITS": "ENGINS"
    },
    "WHEEL EXCAVATOR": {
        "Marchandise2": "WHEEL EXCAVATOR",
        "Modele": "HW210",
        "Détails PRODUITS": "EXCAVATEURS",
        "PRODUITS": "ENGINS"
    },
    "EXCAVOTOR": {
        "Marchandise2": "EXCAVOTOR",
        "Modele": "HX340HD",
        "Détails PRODUITS": "EXCAVATEURS",
        "PRODUITS": "ENGINS"
    },
    "PELLE SUR PNEU": {
        "Marchandise2": "PELLE SUR PNEU",
        "Modele": "A918",
        "Détails PRODUITS": "EXCAVATEURS",
        "PRODUITS": "ENGINS"
    },
    "PELLE SUR CHENILLE": {
        "Marchandise2": "PELLE SUR CHENILLE",
        "Modele": "R930",
        "Détails PRODUITS": "EXCAVATEURS",
        "PRODUITS": "ENGINS"
    },

    # ─── BULLDOZERS ────────────────────────────────────────────────────
    "BULLDOZER": {
        "Marchandise2": "BULLDOZER",
        "Modele": "SD32D",
        "Détails PRODUITS": "BULLDOZERS",
        "PRODUITS": "ENGINS"
    },

    # ─── WHEEL LOADERS ─────────────────────────────────────────────────
    "WHEEL LOADER": {
        "Marchandise2": "WHEEL LOADER",
        "Modele": "ZL50GN",
        "Détails PRODUITS": "CHARGEURS",
        "PRODUITS": "ENGINS"
    },

    # ─── COMPACTORS / ROLLERS ──────────────────────────────────────────
    "ROAD ROLLER": {
        "Marchandise2": "ROAD ROLLER",
        "Modele": "XS203J",
        "Détails PRODUITS": "COMPACTEURS",
        "PRODUITS": "ENGINS"
    },
    "ROLLER": {
        "Marchandise2": "ROLLER",
        "Modele": "XP163",
        "Détails PRODUITS": "COMPACTEURS",
        "PRODUITS": "ENGINS"
    },
    "COMPACTOR": {
        "Marchandise2": "COMPACTOR",
        "Modele": "XS203J",
        "Détails PRODUITS": "COMPACTEURS",
        "PRODUITS": "ENGINS"
    },
    "PNEUMATIC TIRE ROLLER": {
        "Marchandise2": "PNEUMATIC TIRE ROLLER",
        "Modele": "XP263",
        "Détails PRODUITS": "COMPACTEURS",
        "PRODUITS": "ENGINS"
    },
    "PNEUMATIC ROLLER": {
        "Marchandise2": "PNEUMATIC ROLLER",
        "Modele": "XP263S",
        "Détails PRODUITS": "COMPACTEURS",
        "PRODUITS": "ENGINS"
    },
    "SINGLE DRUM ROAD ROLLER": {
        "Marchandise2": "SINGLE DRUM ROAD ROLLER",
        "Modele": "XS203J",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },
    "MIX COMPACTOR": {
        "Marchandise2": "MIX COMPACTOR",
        "Modele": "XS143J",
        "Détails PRODUITS": "CAMIONS",
        "PRODUITS": "LOURD"
    },

    # ─── PAVERS / FINISHERS ────────────────────────────────────────────
    "PAVER": {
        "Marchandise2": "PAVER",
        "Modele": "RP603",
        "Détails PRODUITS": "FINISSEUR",
        "PRODUITS": "ENGINS"
    },
    "CRAWLER ASPHALT PAVER": {
        "Marchandise2": "CRAWLER ASPHALT PAVER",
        "Modele": "RP603",
        "Détails PRODUITS": "FINISSEUR",
        "PRODUITS": "ENGINS"
    },

    # ─── CRANES ────────────────────────────────────────────────────────
    "CRANE": {
        "Marchandise2": "CRANE",
        "Modele": "QY50KD",
        "Détails PRODUITS": "CAMION GRUE",
        "PRODUITS": "ENGINS"
    },
    "MOBILE CRANE": {
        "Marchandise2": "MOBILE CRANE",
        "Modele": "QY25K5D",
        "Détails PRODUITS": "CAMION GRUE",
        "PRODUITS": "ENGINS"
    },
    "TRUCK CRANE": {
        "Marchandise2": "TRUCK CRANE",
        "Modele": "QY50KD",
        "Détails PRODUITS": "CAMION GRUE",
        "PRODUITS": "ENGINS"
    },
    "TRUCK MOUNTED CRANE": {
        "Marchandise2": "TRUCK MOUNTED CRANE",
        "Modele": "1929AP DRIVE",
        "Détails PRODUITS": "CAMION GRUE",
        "PRODUITS": "ENGINS"
    },

    # ─── FORKLIFTS ─────────────────────────────────────────────────────
    "FORKLIFT": {
        "Marchandise2": "FORKLIFT",
        "Modele": "CPCD30",
        "Détails PRODUITS": "CHARIOT ELEVATEUR",
        "PRODUITS": "ENGINS"
    },

    # ─── MOTOR GRADER ──────────────────────────────────────────────────
    "MOTOR GRADER": {
        "Marchandise2": "MOTOR GRADER",
        "Modele": "GR215",
        "Détails PRODUITS": "NIVELEUSES",
        "PRODUITS": "ENGINS"
    },
}


# ── Priority ordering for multi-word keywords ──────────────────────────────────
# Longer / more-specific keywords must be checked before shorter ones so that
# e.g. "CRAWLER EXCAVATOR" is matched before the bare "EXCAVATOR" rule.
SORTED_RULES = sorted(RULES.keys(), key=lambda k: len(k.split()), reverse=True)


def apply_dictionary(text):
    """
    Try to match the input text against every keyword in RULES.
    Keywords are evaluated longest-first so more-specific phrases take
    precedence over shorter overlapping ones.

    Returns a dict with the matched classification or None.
    """
    norm = normalize(text)

    for keyword in SORTED_RULES:
        norm_kw = normalize(keyword)
        # Use word-boundary-aware matching to avoid false sub-string hits
        pattern = r'\b' + re.escape(norm_kw) + r'\b'
        if re.search(pattern, norm):
            values = RULES[keyword]
            return {
                "Marchandise2": values.get("Marchandise2", ""),
                "Modele":       values.get("Modele", ""),
                "Details":      values.get("Détails PRODUITS", ""),
                "Produits":     values.get("PRODUITS", ""),
                "source":       "dictionary"
            }

    return None
