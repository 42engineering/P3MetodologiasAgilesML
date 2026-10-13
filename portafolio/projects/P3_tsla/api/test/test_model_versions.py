import json
import zipfile

from P3_tsla.api.constants import MODELS_DIR

modelPath = MODELS_DIR / "PT1_1_TSLA_5DAYS_LSTM.keras"

with zipfile.ZipFile(modelPath, "r") as modelFile:

    metadata = json.loads(modelFile.read("metadata.json"))
    print("Keras version:", metadata.get("keras_version"))
    print("Date saved:", metadata.get("date_saved"))