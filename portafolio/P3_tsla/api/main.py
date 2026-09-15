from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from P3_tsla.api.predict import router
from P3_tsla.api.constants import PIPELINE_NAME


app = FastAPI(
    title=PIPELINE_NAME,
    version="1.0.0",
    description="""
    API REST para inferencia histórica
    del modelo PT1_1_TSLA_30DAYS_LSTM.keras
    """
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# -------------------------
# API
# -------------------------

app.include_router(router)


# -------------------------
# FRONTEND
# -------------------------

FRONTEND_DIR = (
    Path(__file__).resolve().parents[1]
    / "frontend"
)

app.mount(
    "/",
    StaticFiles(
        directory=FRONTEND_DIR,
        html=True
    ),
    name="frontend"
)