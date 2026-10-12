import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from P3_tsla.api.predict import router
from P3_tsla.api.constants import PIPELINE_NAME


corsOrigins = os.getenv(
    "CORS_ORIGINS",
    "https://portafolioml1.vercel.app"
).split(",")
corsOrigins = [origin.strip() for origin in corsOrigins if origin.strip()]

app = FastAPI(
    title=PIPELINE_NAME,
    version="1.0.0",
    description="API REST para inferencia histórica de la accion de TSLA"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=corsOrigins,
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