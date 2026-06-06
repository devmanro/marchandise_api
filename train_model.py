import pandas as pd
import re
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline


def clean_text(text):
    text = str(text).upper()
    text = re.sub(r'[^A-Z0-9 ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# ✅ Load your training file
df = pd.read_excel("training.xlsx")

# Clean input
df["Marchandise"] = df["Marchandise"].fillna("").astype(str).apply(clean_text)

# Target columns
target_cols = ["Marchandise2", "Modèle", "Détails PRODUITS", "PRODUITS"]

df[target_cols] = df[target_cols].fillna("UNKNOWN").astype(str)

X = df["Marchandise"]
y = df[target_cols]


# ✅ Build model
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        ngram_range=(1,2),
        max_features=6000
    )),
    ("clf", MultiOutputClassifier(
        RandomForestClassifier(
            n_estimators=200,
            max_depth=30,
            n_jobs=-1
        )
    ))
])



print(df.dtypes)

print("Training model...")
model.fit(X, y)

joblib.dump(model, "marchandise_model.pkl")

print("✅ Model saved as marchandise_model.pkl")