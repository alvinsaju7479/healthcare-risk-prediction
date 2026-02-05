import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

IN_PATH = Path("data/processed/processed.csv")
OUT_DIR = Path("data/processed")

def main():
    df = pd.read_csv(IN_PATH)
    y = df["target"]
    X = df.drop(columns=["target"])

    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp
    )

    X_train.assign(target=y_train).to_csv(OUT_DIR/"train.csv", index=False)
    X_val.assign(target=y_val).to_csv(OUT_DIR/"val.csv", index=False)
    X_test.assign(target=y_test).to_csv(OUT_DIR/"test.csv", index=False)

    print("Saved train/val/test splits.")

if __name__ == "__main__":
    main()
