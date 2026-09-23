[Volver al README](/portafolio/projects/P3_tsla/README.md)

# Despliegue de modelos

## Infraestructura

### Nombre del modelo

PT1_1_TSLA_30DAYS_LSTM.h5

### Despliegue com frontend

- https://tslastockpredictormain.vercel.app/

### Swager backend
- https://p3metodologiasagilesml-1.onrender.com/docs

### Vercel framework

- https://vercel.com/42engineering-projects/tsla_stock_predictor_main

### Plataforma de despliegue

- Backend API: Fast- API- Render
- Frontend: Vercel
- Control de versiones: GitHub, DVC, MLflow
- 
- Contenerización: Docker

### Requisitos técnicos

- Python
- TensorFlow \
- FastAPI 
- Uvicorn 0.34.0
- NumPy 
- Pandas 
- Scikit-learn 
- Docker
- Git
- Dvc
- Mlflow



### Diagrama de arquitectura

```md
### Diagrama de arquitectura desplegada

```text
Usuario
   ↓
Frontend
(HTML + CSS + JavaScript)
(Vercel)
   ↓
REST API FastAPI
(Render)
   ↓
Endpoint /models
(Lista de modelos disponibles)
   ↓
Endpoint /predict
(Fecha + Modelo seleccionado)
   ↓
Model Loader
(getModel)
   ↓
TensorFlow CPU
   ↓
Modelo seleccionado dinámicamente

   ↓
MinMaxScaler
(minmax_scaler.pkl)
   ↓
TeslaData.csv
   ↓
Predicción de movimiento bursátil TSLA
(Probabilidad + Dirección)
```




```

---

## Código de despliegue

### Archivo principal

`P3_tsla/api/main.py`

### Rutas de acceso a los archivos

```md
deployment/Dockerfile
deployment/docker-compose.yml
P3_tsla/api/main.py
P3_tsla/api/predict.py
P3_tsla/api/model_loader.py
P3_tsla/api/utils.py
models/PT1_1_TSLA_30DAYS_LSTM.keras
pyproject.toml
frontend/index.html
frontend/style.css
frontend/script.js
```

### Variables de entorno

```md
PORT
PYTHON_VERSION
RENDER_EXTERNAL_URL
```

---

## Documentación del despliegue

### Instrucciones de instalación

1. Clonar el repositorio GitHub:

```bash
git clone https://github.com/42engineering/P3MetodologiasAgilesML
```

2. Entrar al proyecto:

```bash
cd tdsp_template
```

3. Instalar dependencias:

```bash
pip install -e .
```

4. Verificar instalación TensorFlow:

```bash
python -c "import tensorflow as tf; print(tf.__version__)"
```

---

### Instrucciones de configuración

1. Configurar Dockerfile ubicado en:

```md
deployment/Dockerfile
```

2. Configurar docker-compose:

```md
deployment/docker-compose.yml
```

3. Configurar URL backend en:

```md
frontend/script.js
```

reemplazando:

```javascript
https://p3metodologiasagilesml.onrender.com/
```

por la URL real del servicio Render.

4. Configurar Render:

```md
Root Directory: tdsp_template
Docker Build Context Directory: .
Dockerfile Path: deployment/Dockerfile
```

5. Configurar Vercel:

```md
Root Directory: frontend
Framework Preset: Other
```

---

### Instrucciones de uso

1. Abrir frontend desplegado en Vercel.
2. Seleccionar fecha inicial para la predicción.
3. Presionar el botón:

```md
Predict Movement
```

4. El frontend enviará la solicitud al endpoint:
```md
POST /predict
```

5. El sistema retornará:
- Predicción bursátil
- Probabilidad estimada
- Movimiento real histórico
- Ventana temporal utilizada

---
### Instrucciones de mantenimiento

- Actualizar dependencias periódicamente desde `pyproject.toml`.
- Verificar logs de Render para monitoreo de errores.
- Validar disponibilidad del servicio Render.
- Actualizar modelo TensorFlow cuando existan nuevas versiones entrenadas.
- Monitorear consumo de memoria y CPU del contenedor Docker.
- Verificar compatibilidad entre TensorFlow y Keras antes de actualizar versiones.
- Mantener respaldos del modelo entrenado y datasets históricos.
- Validar funcionamiento de endpoints usando Swagger:

```md
/docs
```

- Verificar integración frontend-backend después de cada despliegue.
