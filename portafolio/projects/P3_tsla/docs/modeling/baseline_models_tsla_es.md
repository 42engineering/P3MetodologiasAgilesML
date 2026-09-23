[Volver al README](/portafolio/projects/P3_tsla/README_SP.md)

# Objetivo del modelamiento

PT1.1 — Predicción de Dirección Sube/Baja usando LSTM y modelos hibridos LSTM+CNN

Predecir la dirección del precio de cierre de la acción de Tesla (TSLA) para el siguiente día bursátil.

El modelo debe clasificar si:

- el precio subirá (`1`)
- o bajará/no subirá (`0`)

utilizando información histórica del mercado financiero.

---
# Reporte del Modelo Baseline

El modelo baseline corresponde al primer enfoque de aprendizaje mediante LSTM a este modelo se le llamo LSTM1.
Su objetivo es establecer una línea base de desempeño que permita comparar posteriormente arquitecturas más complejas como DeepLSTM1 y CNNLSTM1.

El modelo utiliza una arquitectura LSTM simple para capturar patrones temporales presentes en los datos históricos del mercado financiero. La salida del modelo corresponde a una clasificación binaria que indica si el precio de cierre de la acción aumentará o disminuirá en el siguiente período de análisis.

---

# Descripción del modelo

El modelo baseline implementado corresponde a una arquitectura `LSTM1`, utilizada como primera aproximación para resolver el problema de clasificación binaria sobre la dirección futura del precio de Tesla.

El modelo está compuesto por:

* Una capa LSTM con 64 neuronas.
* Una capa densa de salida con función de activación sigmoide.

La arquitectura fue diseñada para capturar patrones temporales presentes en las series financieras utilizando secuencias históricas de precios y volumen.

---

# Variables de entrada

Las variables utilizadas como entrada del modelo fueron:

* Open
* High
* Low
* Close
* Volume

Estas variables fueron normalizadas utilizando `MinMaxScaler` y posteriormente transformadas en secuencias temporales para el entrenamiento de la red neuronal.

# Variable objetivo
Se emplearon difetente series de tiempo para lo que planteo un configuracionse de [5, 10, 15, 20, 30] dias.

---https://chatgpt.com/g/g-p-6a067a71c9508191b761906706e43f36/c/6a22532d-5980-83eb-bd21-efec1732c6a9

# Variable objetivo

La variable objetivo utilizada fue:

* `SubeBaja`

Esta variable representa la dirección futura del precio de cierre de Tesla:

* `1`: el precio subirá.
* `0`: el precio bajará o permanecerá igual.

La variable fue generada comparando el precio de cierre actual con el precio de cierre del siguiente día bursátil.

# Evaluación del modelo

## Métricas de evaluación

Las métricas utilizadas para evaluar el rendimiento del modelo fueron:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

Estas métricas permiten evaluar la capacidad del modelo para clasificar correctamente la dirección del precio de la acción.

---

## Resultados de evaluación

| Modelo     | Accuracy | Loss                | Observaciones                                                  |
| ---------- | -------- | ------------------- | -------------------------------------------------------------- |
| SimpleLSTM | ~0.5    | Binary Crossentropy | Rendimiento cercano al azar, pero útil como línea base inicial |

El modelo obtuvo un accuracy cercano al 52%, indicando una capacidad limitada para predecir correctamente la dirección futura del precio. Por lo que se procedio a


---

# Análisis de los resultados

El modelo baseline permitió validar el funcionamiento completo del pipeline de entrenamiento, evaluación y predicción utilizando datos financieros de Tesla. La arquitectura LSTM logró capturar parcialmente patrones temporales presentes en la serie de tiempo.

Sin embargo, el rendimiento obtenido fue limitado debido a la alta volatilidad y complejidad inherente de los mercados financieros. El accuracy cercano al 50% sugiere que el modelo aún presenta dificultades para generalizar patrones predictivos robustos.

Entre las principales debilidades del modelo se encuentran:

* Arquitectura relativamente simple.
* Limitada profundidad de aprendizaje.
* Sensibilidad al ruido financiero.
* Ausencia de variables técnicas adicionales.

---

# Conclusiones

El modelo `SimpleLSTM` funcionó como una línea base adecuada para el proyecto y permitió establecer un punto de comparación para arquitecturas más complejas.

Los resultados muestran que la predicción de movimientos bursátiles es un problema altamente complejo y no lineal. Como posibles mejoras futuras se recomienda:

* Utilizar arquitecturas LSTM más profundas.
* Incorporar capas Dropout y técnicas de regularización.
* Incluir indicadores técnicos financieros.
* Ajustar hiperparámetros.
* Incrementar el tamaño y diversidad de los datos históricos.

---

# Referencias

* Yahoo Finance (`yfinance`) – Fuente de datos financieros históricos de Tesla.
* TensorFlow/Keras – Implementación de redes neuronales LSTM.
* Scikit-learn – Preprocesamiento, normalización y métricas de evaluación.
* MLflow – Seguimiento y registro de experimentos de machine learning.
