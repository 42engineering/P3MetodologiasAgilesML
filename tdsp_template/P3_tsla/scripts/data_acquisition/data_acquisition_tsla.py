import os
import yfinance as yf
import pandas as pd

def dataTeslaCsv():

    filePath = "data/raw/TeslaData.csv"
    os.makedirs("data/raw", exist_ok=True)

    if os.path.exists(filePath):
        print(f"El archivo ya existe: {filePath}")
        df = pd.read_csv(filePath)

        return df

    print("Descargando datos desde Yahoo Finance...")
    df = yf.download(
        "TSLA",
        start="2015-01-01",
        end="2025-12-31"
    )

    df.to_csv(filePath)
    print(f"Archivo guardado en: {filePath}")
    return df


if __name__ == "__main__":
    df = dataTeslaCsv()
    print(df.head())