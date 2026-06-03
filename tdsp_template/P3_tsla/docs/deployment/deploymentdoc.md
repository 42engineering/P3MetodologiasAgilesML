[Volver al README](../../../../README.md)

# Despliegue de modelos

## Infraestructura

### Nombre del modelo

PT1_1_TSLA_30DAYS_LSTM.h5

### Plataforma de despliegue

- Backend API: Render
- Frontend: Vercel
- Control de versiones: GitHub
- Contenerización: Docker

### Requisitos técnicos

- Python 3.12
- TensorFlow 2.20.0
- FastAPI 0.115.12
- Uvicorn 0.34.0
- NumPy 1.26.4
- Pandas 2.2.2
- Scikit-learn 1.6.1
- Docker
- Git
- Navegador web moderno
- Conexión a internet


### Diagrama de arquitectura

```md
Usuario
   ↓
Frontend FE_TSLA_V1_0 (Vercel)
   ↓
FastAPI REST API (Render)
   ↓
TensorFlow CPU
   ↓
Modelo LSTM PT1_1_TSLA_30DAYS_LSTM
   ↓
Predicción bursátil TSLA
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
