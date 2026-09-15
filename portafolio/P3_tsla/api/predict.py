from fastapi import APIRouter
from pydantic import BaseModel
import numpy as np
import pandas as pd
import traceback

from P3_tsla.api.utils import getWindowFromDate
from P3_tsla.api.scaler_loader import scaler5, scaler10
from P3_tsla.api.model_loader import getModel

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

    return {
        "models":
        list(
            AVAILABLE_MODELS.keys()
        )
    }

@router.post("/predict")
def predict(
    request: PredictionRequest
):

    try:

        print("=" * 50)
        print("REQUEST RECIBIDO")
        print(request)
        print("=" * 50)

        if request.model_name not in AVAILABLE_MODELS:

            return {
                "error":
                f"Unknown model: {request.model_name}"
            }

        modelFile = AVAILABLE_MODELS[
            request.model_name
        ]

        modelPath = (
            MODELS_DIR /
            modelFile
        )

        sequenceLength = int(
            modelFile.split("_")[3]
            .replace("DAYS", "")
        )

        features = MODEL_FEATURES[
            request.model_name
        ]

        print(
            "MODEL:",
            modelFile
        )

        print(
            "SEQUENCE_LENGTH:",
            sequenceLength
        )

        print(
            "FEATURES:",
            features
        )

        model = getModel(
            modelPath
        )

        window = getWindowFromDate(
            request.start_date,
            sequenceLength
        )

        print(
            "WINDOW SHAPE:",
            window.shape
        )

        xInput = window[features].values

        print("X ORIGINAL:",xInput.shape)

        if len(features) == 5:
            scaler = scaler5
        else:
            scaler = scaler10

        xInput = scaler.transform(
            xInput
        )

        xInput = np.expand_dims(
            xInput,
            axis=0
        )

        print(
            "X FINAL:",
            xInput.shape
        )

        prediction = model.predict(
            xInput,
            verbose=0
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
            if float(
                window.iloc[-1]["Close"]
            ) >
            float(
                window.iloc[-2]["Close"]
            )
            else "BAJÓ"
        )

        if "Date" in window.columns:

            windowStart = str(
                window.iloc[0]["Date"]
            )

            windowEnd = str(
                window.iloc[-1]["Date"]
            )

        elif "date" in window.columns:

            windowStart = str(
                window.iloc[0]["date"]
            )

            windowEnd = str(
                window.iloc[-1]["date"]
            )

        else:

            windowStart = str(
                window.index[0]
            )

            windowEnd = str(
                window.index[-1]
            )

        return {

            "model":
            request.model_name,

            "sequence_length":
            sequenceLength,

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
            "error":
            str(e)
        }

@router.get("/latest-window")
def latestWindow():

    df = pd.read_csv(
        CSV_PATH
    )

    return {
        "rows":
        len(df)
    }

@router.get("/health")
def health():

    return {

        "status":
        "running",

        "pipeline":
        PIPELINE_NAME,

        "available_models":
        len(
            AVAILABLE_MODELS
        ),

        "framework":
        "TensorFlow"
    }