import pandas as pd

from P3_tsla.api.constants import (
    CSV_PATH,
    SEQUENCE_LENGTH
)


def getWindowFromDate(
    startDate: str
):

    df = pd.read_csv(
        CSV_PATH
    )


    if 'Date' in df.columns:

        dateColumn = 'Date'

    elif 'date' in df.columns:

        dateColumn = 'date'

    else:

        raise Exception(
            "No date column found"
        )

    df[dateColumn] = pd.to_datetime(
        df[dateColumn]
    )

    startDate = pd.to_datetime(
        startDate
    )
    filtered = df[
        df[dateColumn] >= startDate
    ]

    if len(filtered) < SEQUENCE_LENGTH:

        raise Exception(
            f"Not enough rows after {startDate}"
        )

    window = filtered.head(
        SEQUENCE_LENGTH
    )

    return window