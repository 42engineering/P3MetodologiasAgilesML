from fastapi import APIRouter
from pydantic import BaseModel

import numpy as np
import pandas as pd
import traceback

from P3_tsla.api.model_loader import model
from P3_tsla.api.utils import getWindowFromDate

from P3_tsla.api.constants import (
    FEATURES,
    CSV_PATH,
    SEQUENCE_LENGTH,
    PIPELINE_NAME,
    MODEL_NAME
)

router = APIRouter()


class PredictionRequest(BaseModel):

    start_date: str


@router.post("/predict")
def predict(
    request: PredictionRequest
):

    try:

        print("=" * 50)
        print("REQUEST RECIBIDO")
        print(request)
        print("=" * 50)

        print("1. Obteniendo ventana...")

        window = getWindowFromDate(
            request.start_date
        )

        print("COLUMNAS DEL WINDOW:")
        print(window.columns)

        print("Ventana obtenida")
        print(window.head())

        print("2. Construyendo xInput...")

        xInput = window[
            FEATURES
        ].values

        print(
            "Shape antes expand_dims:",
            xInput.shape
        )

        xInput = np.expand_dims(
            xInput,
            axis=0
        )

        print(
            "Shape final:",
            xInput.shape
        )

        print(
            "3. Ejecutando predicción..."
        )

        prediction = model.predict(
            xInput
        )

        print(
            "Predicción cruda:",
            prediction
        )

        probability = float(
            prediction[0][0]
        )

        predictionLabel = (
            "SUBIRÁ"
            if probability > 0.5
            else "BAJARÁ"
        )

        realMovement = (
            "SUBIÓ"
            if window.iloc[-1]['Close']
            >
            window.iloc[-2]['Close']
            else "BAJÓ"
        )

        # ---------------------------------
        # MANEJO ROBUSTO FECHAS
        # ---------------------------------

        if 'Date' in window.columns:

            windowStart = str(
                window.iloc[0]['Date']
            )

            windowEnd = str(
                window.iloc[-1]['Date']
            )

        elif 'date' in window.columns:

            windowStart = str(
                window.iloc[0]['date']
            )

            windowEnd = str(
                window.iloc[-1]['date']
            )

        else:

            windowStart = str(
                window.index[0]
            )

            windowEnd = str(
                window.index[-1]
            )

        print(
            "Predicción completada correctamente"
        )

        return {

            "prediction":
            predictionLabel,

            "probability":
            probability,

            "real_movement":
            realMovement,

            "window_start":
            windowStart,

            "window_end":
            windowEnd
        }

    except Exception as e:

        print("=" * 50)
        print("ERROR EN /predict")
        print(str(e))
        traceback.print_exc()
        print("=" * 50)

        return {
            "error": str(e)
        }


@router.get("/latest-window")
def latestWindow():

    df = pd.read_csv(CSV_PATH)

    latest = df.tail(SEQUENCE_LENGTH)

    return {

        "sequence_length":
        SEQUENCE_LENGTH,

        "values":
        latest.to_dict(
            orient="records"
        )
    }


@router.get("/health")
def health():

    return {

        "status": "running",

        "pipeline":
        PIPELINE_NAME,

        "model":
        MODEL_NAME,

        "sequence_length":
        SEQUENCE_LENGTH,

        "framework":
        "TensorFlow"
    }