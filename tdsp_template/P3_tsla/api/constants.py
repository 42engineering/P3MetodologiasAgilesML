from pathlib import Path

P3_TSLA_ROOT = Path(__file__).resolve().parents[1]

CSV_PATH = (
    P3_TSLA_ROOT /
    "data" /
    "raw" /
    "TeslaData.csv"
)

MODEL_PATH = (
    P3_TSLA_ROOT.parent /
    "models" /
    "PT1_1_TSLA_30DAYS_LSTM.keras"
)

PIPELINE_NAME = "Pipeline DesplieguePT1.1NE"

MODEL_NAME = "PT1_1_TSLA_30DAYS_LSTM.keras"

SEQUENCE_LENGTH = 30

FEATURES = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume"
]