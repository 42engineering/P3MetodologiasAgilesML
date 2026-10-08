import os
import yfinance as yf
import pandas as pd

from P3_tsla.api.constants import CSV_PATH

def dataTeslaCsv():
    os.makedirs("data/raw", exist_ok=True)

    if os.path.exists(CSV_PATH):
        print(f"El archivo ya existe: {CSV_PATH}")
        df = pd.read_csv(CSV_PATH)

        return df

    print("Descargando datos desde Yahoo Finance...")
    df = yf.download(
        "TSLA",
        start="2015-01-01",
        end="2025-12-31"
    )

    df.to_csv(CSV_PATH)
    print(f"Archivo guardado en: {CSV_PATH}")
    return df


if __name__ == "__main__":
    df = dataTeslaCsv()
    print(df.head())