PIPELINE_NAME = (
    "Pipeline DesplieguePT1.1NE"
)

MODEL_NAME = (
    "PT1_1_TSLA_30DAYS_LSTM.h5"
)

MODEL_PATH = (
    "models/"
    "PT1_1_TSLA_30DAYS_LSTM.h5"
)

CSV_PATH = (
    "data/raw/TeslaData.csv"
)

SEQUENCE_LENGTH = 30

FEATURES = [
    'Open',
    'High',
    'Low',
    'Close',
    'Volume'
]
