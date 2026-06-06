from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
import os
import requests
import gdown

from dictionary_rules import apply_dictionary

app = FastAPI()

MODEL_PATH = "marchandise_model.pkl"
FILE_ID = "https://drive.google.com/file/d/1SU532bppGcmOCX_SJnsZgdKmx3jzuwCI/view?usp=drivesdk"

def download_model():
    if not os.path.exists(MODEL_PATH):
        print("📥 Downloading model from Google Drive...")
        url = f"https://drive.google.com/uc?id={FILE_ID}"
        gdown.download(url, MODEL_PATH, quiet=False)
        print("✅ Model downloaded!")

download_model()

print("Loading model...")
model = joblib.load(MODEL_PATH)
print("✅ Model loaded")



class Item(BaseModel):
    marchandise: str


class BatchRequest(BaseModel):
    rows: List[Item]


@app.post("/predict")
def predict_batch(data: BatchRequest):

    texts = [row.marchandise for row in data.rows]

    results = []

    for text in texts:

        # 1️⃣ Try dictionary first
        rule_result = apply_dictionary(text)

        if rule_result:
            results.append(rule_result)
            continue

        # 2️⃣ Otherwise use ML
        pred = model.predict([text])[0]

        results.append({
            "Marchandise2": pred[0],
            "Modele": pred[1],
            "Details": pred[2],
            "Produits": pred[3],
            "source": "ml"
        })

    return {"predictions": results}
