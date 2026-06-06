import joblib

from P3_tsla.api.constants import (
    SCALER_PATH_5,
    SCALER_PATH_10
)

scaler5 = joblib.load(
    SCALER_PATH_5
)

scaler10 = joblib.load(
    SCALER_PATH_10
)

print(
    "Scaler 5 features loaded"
)

print(
    "Scaler 10 features loaded"
)