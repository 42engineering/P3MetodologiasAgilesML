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

FEATURES = ["Open","High","Low","Close","Volume"]

FEATURES_INDICADORES1 = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "RSI_14",
    "MACD",
    "MACD_SIGNAL",
    "ATR_14",
    "EMA_20"
]

SCALER_PATH_5 = (
    MODELS_DIR /
    "minmax_scaler.pkl"
)

SCALER_PATH_10 = (
    MODELS_DIR /
    "minmax_scaler_indicadores1.pkl"
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

    # "DeepLSTM1_Indicadores1_5":
    # "PT1_1_TSLA_5DAYS_DeepLSTM1_INDICADORES1.keras",

    # "DeepLSTM1_Indicadores1_10":
    # "PT1_1_TSLA_10DAYS_DeepLSTM1_INDICADORES1.keras",

    # "DeepLSTM1_Indicadores1_15":
    # "PT1_1_TSLA_15DAYS_DeepLSTM1_INDICADORES1.keras",

    # "DeepLSTM1_Indicadores1_20":
    # "PT1_1_TSLA_20DAYS_DeepLSTM1_INDICADORES1.keras",

    "CNNLSTM1_5":
    "PT1_1_TSLA_5DAYS_CNNLSTM1.keras",

    "CNNLSTM1_10":
    "PT1_1_TSLA_10DAYS_CNNLSTM1.keras",

    "CNNLSTM1_15":
    "PT1_1_TSLA_15DAYS_CNNLSTM1.keras",

    "CNNLSTM1_20":
    "PT1_1_TSLA_20DAYS_CNNLSTM1.keras"
}

MODEL_FEATURES = {

    "LSTM_5": FEATURES,
    "LSTM_10": FEATURES,
    "LSTM_15": FEATURES,
    "LSTM_20": FEATURES,
    "LSTM_30": FEATURES,

    "LSTM1_5": FEATURES,
    "LSTM1_10": FEATURES,
    "LSTM1_15": FEATURES,
    "LSTM1_20": FEATURES,

    "DeepLSTM1_5": FEATURES,
    "DeepLSTM1_10": FEATURES,
    "DeepLSTM1_15": FEATURES,
    "DeepLSTM1_20": FEATURES,

    "CNNLSTM1_5": FEATURES,
    "CNNLSTM1_10": FEATURES,
    "CNNLSTM1_15": FEATURES,
    "CNNLSTM1_20": FEATURES,

    # "DeepLSTM1_Indicadores1_5":
    # FEATURES_INDICADORES1,

    # "DeepLSTM1_Indicadores1_10":
    # FEATURES_INDICADORES1,

    # "DeepLSTM1_Indicadores1_15":
    # FEATURES_INDICADORES1,

    # "DeepLSTM1_Indicadores1_20":
    # FEATURES_INDICADORES1
}