FROM python:3.10.12

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -e .

EXPOSE 8000

CMD ["uvicorn",
     "P3_tsla.api.main:app",
     "--host",
     "0.0.0.0",
     "--port",
     "8000"]