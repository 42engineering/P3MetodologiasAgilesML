import joblib

from P3_tsla.api.constants import (
    SCALER_PATH
)

scaler = joblib.load(
    SCALER_PATH
)