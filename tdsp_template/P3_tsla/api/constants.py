from pathlib import Path

P3_TSLA_ROOT = Path(__file__).resolve().parents[1]

MODELS_DIR = (
    P3_TSLA_ROOT.parent /
    "models"
)

CSV_PATH = (
    P3_TSLA_ROOT /
    "data" /
    "raw" /
    "TeslaData.csv"
)

DEFAULT_MODEL_NAME = (
    "PT1_1_TSLA_30DAYS_LSTM.keras"
)

MODEL_PATH = (
    MODELS_DIR /
    DEFAULT_MODEL_NAME
)

PIPELINE_NAME = (
    "Pipeline DesplieguePT1.1NE"
)

MODEL_NAME = DEFAULT_MODEL_NAME

SEQUENCE_LENGTH = 30

FEATURES = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume"
]

SCALER_PATH = (
    MODELS_DIR /
    "minmax_scaler.pkl"
)

AVAILABLE_MODELS = {

    "LSTM_5":
    "PT1_1_TSLA_5DAYS_LSTM.keras",

    "LSTM_10":
    "PT1_1_TSLA_10DAYS_LSTM.keras",

    "LSTM_15":
    "PT1_1_TSLA_15DAYS_LSTM.keras",

    "LSTM_20":
    "PT1_1_TSLA_20DAYS_LSTM.keras",

    "LSTM_30":
    "PT1_1_TSLA_30DAYS_LSTM.keras",

    "LSTM1_5":
    "PT1_1_TSLA_5DAYS_LSTM1.keras",

    "LSTM1_10":
    "PT1_1_TSLA_10DAYS_LSTM1.keras",

    "LSTM1_15":
    "PT1_1_TSLA_15DAYS_LSTM1.keras",

    "LSTM1_20":
    "PT1_1_TSLA_20DAYS_LSTM1.keras",

    "DeepLSTM1_5":
    "PT1_1_TSLA_5DAYS_DeepLSTM1.keras",

    "DeepLSTM1_10":
    "PT1_1_TSLA_10DAYS_DeepLSTM1.keras",

    "DeepLSTM1_15":
    "PT1_1_TSLA_15DAYS_DeepLSTM1.keras",

    "DeepLSTM1_20":
    "PT1_1_TSLA_20DAYS_DeepLSTM1.keras",

    "DeepLSTM1_Indicadores1_5":
    "PT1_1_TSLA_5DAYS_DeepLSTM1_INDICADORES1.keras",

    "DeepLSTM1_Indicadores1_10":
    "PT1_1_TSLA_10DAYS_DeepLSTM1_INDICADORES1.keras",

    "DeepLSTM1_Indicadores1_15":
    "PT1_1_TSLA_15DAYS_DeepLSTM1_INDICADORES1.keras",

    "DeepLSTM1_Indicadores1_20":
    "PT1_1_TSLA_20DAYS_DeepLSTM1_INDICADORES1.keras",

    "CNNLSTM1_5":
    "PT1_1_TSLA_5DAYS_CNNLSTM1.keras",

    "CNNLSTM1_10":
    "PT1_1_TSLA_10DAYS_CNNLSTM1.keras",

    "CNNLSTM1_15":
    "PT1_1_TSLA_15DAYS_CNNLSTM1.keras",

    "CNNLSTM1_20":
    "PT1_1_TSLA_20DAYS_CNNLSTM1.keras"
}