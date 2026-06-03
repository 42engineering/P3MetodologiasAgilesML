import pandas as pd

from P3_tsla.api.constants import (
    CSV_PATH,
    SEQUENCE_LENGTH
)

def getWindowFromDate(startDate:str):

    df = pd.read_csv(CSV_PATH)

    df['Date'] = pd.to_datetime(
        df['Date']
    )

    df = df.sort_values("Date")

    startIndex = df[
        df['Date'] == startDate
    ].index[0]

    window = df.iloc[
        startIndex:startIndex+SEQUENCE_LENGTH
    ]

    return window