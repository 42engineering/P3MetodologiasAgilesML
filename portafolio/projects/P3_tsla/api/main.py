from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    allow_origins=[
        "https://portafolioml1.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {
        "status": "running",
        "pipeline": PIPELINE_NAME,
        "docs": "/docs",
        "health": "/health"
    }


app.include_router(router)