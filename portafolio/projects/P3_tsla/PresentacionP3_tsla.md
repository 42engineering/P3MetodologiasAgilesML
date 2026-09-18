[Volver al README](../../../../README.md)

# Predicción de Dirección Financiera de la accion de TSLA mediante Redes Neuronales
---

###  Objetivo 
Diseñar, entrenar y desplegar un modelo de aprendizaje profundo que permita predecir la dirección del precio de cierre de la acción de Tesla utilizando datos históricos de mercado.

- [Notebook](https://colab.research.google.com/github/42engineering/P3MetodologiasAgilesML/blob/main/portafolio/projects/P3_tsla/scripts/data_acquisition/PT1.1ColabV2.ipynb#scrollTo=A6qEKHZACutI) - Notebook.

### Plataforma de despliegue

- Backend API: Fast- API- Render
- Frontend: Vercel
- Control de versiones: GitHub, DVC, MLflow
- Contenerización: Docker

### Requisitos técnicos

- Python
- TensorFlow 
- FastAPI 
- Uvicorn 0.34.0
- Mlflow
- NumPy 
- Pandas 
- Scikit-learn 
- Docker
- Git
- dvc

### Despliegue

# Despliegue com frontend
https://tslastockpredictormain.vercel.app/

# Swager backend
https://p3metodologiasagilesml-1.onrender.com/docs

# Vercel framework
https://vercel.com/42engineering-projects/tsla_stock_predictor_main

# Problemas de infrastructura encontrados:

- Se utilizo la librerias pandas-ta  para general variables financieras en el modelo DeepLStm con indicadores durante el entrenamiento se utilizo una version pandas-ta==0.4.71b0 en `Colab` que sin embargo esa version no esta disponible dede PyPI para ser instalada automaticamente en render.
Posibles soluciones:

- Reincorporar los modelos basados en indicadores técnicos mediante una implementación propia de RSI, MACD, ATR y EMA utilizando únicamente Pandas y NumPy, eliminando dependencias externas que dificulten la portabilidad del sistema
-Incluir el trabajo de colab en el container de docker para evitar problemas de versionamiento.

# Conclusion sobre modelacion:

- La senal de entrenamiento es baja aun usando Indicadores financieros,  es posible incorporar nuevas fuentes de información, tales como indicadores macroeconómicos, sentimiento de noticias financieras o variables derivadas de redes sociales, con el objetivo de enriquecer la capacidad predictiva de los modelos.

- Es posible mejorar la interfase de usuario para incluir las graficas del mercado y los datos en tiempo real para realizar las predicciones.