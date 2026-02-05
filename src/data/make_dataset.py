# src/data/make_dataset.py
from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw/diabetic_data.csv")   # <-- file name
OUT_PATH = Path("data/processed/processed.csv")

def main():
    if not RAW_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {RAW_PATH.resolve()}\n"
            f"➡️ Put diabetic_data.csv inside data/raw/"
        )

    df = pd.read_csv(RAW_PATH)

    # Standardize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # -----------------------------
    # Target (Risk): 30-day readmission
    # readmitted values usually: '<30', '>30', 'NO'
    # We define risk=1 if '<30', else 0
    # -----------------------------
    if "readmitted" not in df.columns:
        raise ValueError("Expected column 'readmitted' not found in the dataset.")

    df["target"] = (df["readmitted"] == "<30").astype(int)
    df = df.drop(columns=["readmitted"])


    # -----------------------------
    # Basic cleaning
    # -----------------------------
    # Drop ID-like columns (not useful + leakage risk)
    drop_cols = [c for c in ["encounter_id", "patient_nbr"] if c in df.columns]
    df = df.drop(columns=drop_cols)

    # Replace '?' with NaN (common in this dataset)
    df = df.replace("?", pd.NA)

    # Optional: drop super-high-missing columns if present
    # (we'll keep it simple now; preprocessing will handle missing)
    df = df.drop_duplicates()

    # Save
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)

    print("✅ Saved processed dataset")
    print(f"Path: {OUT_PATH}")
    print(f"Shape: {df.shape}")
    print(f"Target rate (risk=1): {df['target'].mean():.4f}")

if __name__ == "__main__":
    main()
