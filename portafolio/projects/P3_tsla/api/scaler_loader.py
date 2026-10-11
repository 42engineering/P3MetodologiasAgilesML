import joblib

from P3_tsla.api.constants import SCALER_PATH_5,SCALER_PATH_10


scaler5 = joblib.load(SCALER_PATH_5)
scaler10 = joblib.load(SCALER_PATH_10)

print( "Scaler 5 features loaded")
print("Scaler 10 features loaded")

####

import joblib

from P3_tsla.api.constants import SCALER_PATH_5, SCALER_PATH_10

loadedScalers = {}

def getScaler(featureCount):
    scalerPaths = {
        5: SCALER_PATH_5,
        10: SCALER_PATH_10
    }

    if featureCount not in scalerPaths:
        raise ValueError(f"Unsupported feature count: {featureCount}")

    if featureCount not in loadedScalers:
        scalerPath = scalerPaths[featureCount]
        print(f"Loading scaler: {scalerPath}")
        loadedScalers[featureCount] = joblib.load(scalerPath)

    return loadedScalers[featureCount]
