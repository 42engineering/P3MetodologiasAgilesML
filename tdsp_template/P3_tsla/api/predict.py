from fastapi import APIRouter
from pydantic import BaseModel

import numpy as np
import pandas as pd

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

    start_date:str


@router.post("/predict")

def predict(
    request:PredictionRequest
):

    window = getWindowFromDate(
        request.start_date
    )

    xInput = window[
        FEATURES
    ].values

    xInput = np.expand_dims(
        xInput,
        axis=0
    )

    prediction = model.predict(
        xInput
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

    return {

        "prediction":
        predictionLabel,

        "probability":
        probability,

        "real_movement":
        realMovement,

        "window_start":
        str(window.iloc[0]['Date']),

        "window_end":
        str(window.iloc[-1]['Date'])
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

        "status":"running",

        "pipeline":
        PIPELINE_NAME,

        "model":
        MODEL_NAME,

        "sequence_length":
        SEQUENCE_LENGTH,

        "framework":
        "TensorFlow"
    }