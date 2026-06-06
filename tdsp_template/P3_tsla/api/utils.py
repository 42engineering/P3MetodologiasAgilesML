from pathlib import Path

import pandas as pd

from P3_tsla.api.constants import (
    CSV_PATH
)

def getWindowFromDate(
    startDate: str,
    sequenceLength: int
):

    df = pd.read_csv(
        CSV_PATH,
        skiprows=[1]
    )

    df = df.rename(
        columns={
            "Price":"Date"
        }
    )

    df = df.iloc[1:].copy()

    print("=" * 50)
    print("COLUMNAS")
    print(df.columns.tolist())

    print("=" * 50)
    print("HEAD")
    print(df.head(10))

    print("=" * 50)

    dateColumn = "Date"

    df[dateColumn] = pd.to_datetime(
        df[dateColumn]
    )

    startDate = pd.to_datetime(
        startDate
    )

    filtered = df[
        df[dateColumn] >= startDate
    ]

    if len(filtered) < sequenceLength:

        raise Exception(
            f"Not enough rows after {startDate}"
        )

    window = filtered.head(
        sequenceLength
    )

    print(
        "CSV_PATH =",
        CSV_PATH
    )

    print(
        "EXISTS =",
        Path(CSV_PATH).exists()
    )

    return window