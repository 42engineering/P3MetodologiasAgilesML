
from fastapi import APIRouter
from pydantic import BaseModel
import numpy as np
import pandas as pd
import traceback

from P3_tsla.api.utils import getWindowFromDate  #ventana historica
from P3_tsla.api.model_loader import getModel #obtener modelo

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

@router.get("/models")
def getModels():
    return {"models": list(AVAILABLE_MODELS.keys())}

# Ejecutar predicción con el modelo seleccionado
@router.post("/predict")
def predict(request: PredictionRequest):
    try:

        print("=" * 50)
        print("REQUEST RECIBIDO")
        print(request)
        print("=" * 50)

        
        if request.model_name not in AVAILABLE_MODELS:
            return {"error": f"Unknown model: {request.model_name}"}

        modelFile = AVAILABLE_MODELS[request.model_name]
        modelPath = MODELS_DIR / modelFile

        sequenceLength = int(modelFile.split("_")[3].replace("DAYS", ""))
        features = MODEL_FEATURES[request.model_name]

        print("MODEL:", modelFile)
        print("SEQUENCE_LENGTH:", sequenceLength)
        print("FEATURES:", features)

        model = getModel(modelPath)

        # Obtener ventana histórica según fecha y longitud de secuencia
        window = getWindowFromDate(request.start_date, sequenceLength)
        print("WINDOW SHAPE:", window.shape)
        # Seleccionar variables que necesita el modelo
        xInput = window[features].values

        print("X ORIGINAL:", xInput.shape)

        # CAMBIO: obtener scaler bajo demanda según número de variables
        # getScaler reutiliza el scaler si ya está cargado en memoria
        scaler = getScaler(len(features))

        # Normalizar datos con el scaler correspondiente
        xInput = scaler.transform(xInput)

        # Adaptar dimensiones al formato esperado por la red neuronal
        xInput = np.expand_dims(xInput, axis=0)

        print("X FINAL:", xInput.shape)

        # Ejecutar inferencia con el modelo seleccionado
        prediction = model.predict(xInput, verbose=0)

        # Extraer probabilidad de la predicción
        probability = float(prediction[0][0])

        # Clasificar la dirección prevista del precio
        predictionLabel = "SUBIRÁ" if probability > 0.5 else "BAJARÁ"

        # Calcular movimiento real comparando los dos últimos cierres
        realMovement = "SUBIÓ" if float(window.iloc[-1]["Close"]) > float(window.iloc[-2]["Close"]) else "BAJÓ"

        # Obtener fechas inicial y final según estructura del dataframe
        if "Date" in window.columns:

            windowStart = str(window.iloc[0]["Date"])
            windowEnd = str(window.iloc[-1]["Date"])

        elif "date" in window.columns:

            windowStart = str(window.iloc[0]["date"])
            windowEnd = str(window.iloc[-1]["date"])

        else:

            windowStart = str(window.index[0])
            windowEnd = str(window.index[-1])

        # Devolver resultado de predicción al frontend
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

        # Registrar información del error para diagnóstico
        print("=" * 50)
        print("ERROR EN /predict")
        print(str(e))
        traceback.print_exc()
        print("=" * 50)

        # Mantener el contrato de errores utilizado por el frontend
        return {"error": str(e)}


# Consultar cantidad de registros del dataset histórico
@router.get("/latest-window")
def latestWindow():

    # Leer dataset de Tesla
    df = pd.read_csv(CSV_PATH)

    return {"rows": len(df)}


# Comprobar estado y configuración básica de la API
@router.get("/health")
def health():

    # Devolver estado del servicio sin cargar modelos
    return {
        "status": "running",
        "pipeline": PIPELINE_NAME,
        "available_models": len(AVAILABLE_MODELS),
        "framework": "TensorFlow"
    }
