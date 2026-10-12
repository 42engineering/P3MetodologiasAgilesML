
from fastapi import APIRouter
from pydantic import BaseModel
import numpy as np
import pandas as pd
import traceback
import time
import os

from P3_tsla.api.utils import getWindowFromDate
from P3_tsla.api.model_loader import getModel
from P3_tsla.api.scaler_loader import getScaler

from P3_tsla.api.constants import (
    CSV_PATH,
    PIPELINE_NAME,
    AVAILABLE_MODELS,
    MODELS_DIR,
    MODEL_FEATURES
)

router = APIRouter()


class PredictionRequest(BaseModel):
    start_date: str
    model_name: str


@router.get("/models") #catalogos de modelos
def getModels():

    return {"models": list(AVAILABLE_MODELS.keys())}

@router.post("/predict") #prediccion modelo seleccionado.
def predict(request: PredictionRequest):

    requestStartTime = time.perf_counter()
    try:

        print(f"Process ID: {os.getpid()}", flush=True)
        print("REQUEST RECIBIDO:", request, flush=True)

        if request.model_name not in AVAILABLE_MODELS: #validacion modelo seleccionado.
            return {"error": f"Unknown model: {request.model_name}"}
        modelFile = AVAILABLE_MODELS[request.model_name]
        modelPath = MODELS_DIR / modelFile

        sequenceLength = int(modelFile.split("_")[3].replace("DAYS", ""))
        features = MODEL_FEATURES[request.model_name]

        print("MODEL:", modelFile, flush=True)
        print("SEQUENCE_LENGTH:", sequenceLength, flush=True)
        print("FEATURES:", features, flush=True)

        startTime = time.perf_counter()

        window = getWindowFromDate(request.start_date, sequenceLength)
        xInput = window[features].values

        print("X ORIGINAL:", xInput.shape, flush=True)
        print(f"Window preparation: {time.perf_counter() - startTime:.3f}s", flush=True)

        startTime = time.perf_counter()
        scaler = getScaler(len(features))
        xInput = scaler.transform(xInput)
        xInput = np.expand_dims(xInput, axis=0)

        print("X FINAL:", xInput.shape, flush=True)
        print(f"Scaler preparation: {time.perf_counter() - startTime:.3f}s", flush=True)

        startTime = time.perf_counter()
        model = getModel(modelPath)
        print(f"Model loading/cache: {time.perf_counter() - startTime:.3f}s", flush=True)

        
        startTime = time.perf_counter()

        prediction = model.predict(xInput, verbose=0)

        print(f"Model inference: {time.perf_counter() - startTime:.3f}s", flush=True)


        probability = float(prediction[0][0])
        predictionLabel = "SUBIRÁ" if probability > 0.5 else "BAJARÁ"
        realMovement = "SUBIÓ" if float(window.iloc[-1]["Close"]) > float(window.iloc[-2]["Close"]) else "BAJÓ"

    
        if "Date" in window.columns:

            windowStart = str(window.iloc[0]["Date"])
            windowEnd = str(window.iloc[-1]["Date"])

        elif "date" in window.columns:

            windowStart = str(window.iloc[0]["date"])
            windowEnd = str(window.iloc[-1]["date"])

        else:

            windowStart = str(window.index[0])
            windowEnd = str(window.index[-1])

        return {
            "model": request.model_name,
            "sequence_length": sequenceLength,
            "prediction": predictionLabel,
            "probability": probability,
            "real_movement": realMovement,
            "window_start": windowStart,
            "window_end": windowEnd
        }

    except Exception as e:
        print("ERROR EN /predict:", str(e), flush=True)
        traceback.print_exc()

        return {"error": str(e)}

    finally:
        totalTime = time.perf_counter() - requestStartTime
        print(f"Total prediction time: {totalTime:.3f}s", flush=True)


@router.get("/latest-window")
def latestWindow():
    df = pd.read_csv(CSV_PATH)
    return {"rows": len(df)}


@router.get("/health")
def health():

    return {
        "status": "running",
        "pipeline": PIPELINE_NAME,
        "available_models": len(AVAILABLE_MODELS),
        "framework": "TensorFlow"
    }
