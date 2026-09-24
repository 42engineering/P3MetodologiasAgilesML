[Back to README](../../README_SP.md)

#  (Project Charter) – Comprensión del Negocio

## Nombre del Proyecto

Predicción de la Dirección Financiera de TSLA mediante Redes Neuronales

## Objetivo del Proyecto

El proyecto propone el desarrollo de un modelo híbrido de Deep Learning basado en arquitecturas LSTM para predecir el comportamiento de la acción de Tesla (TSLA), utilizando exclusivamente datos históricos del mercado e indicadores técnicos financieros.

## Beneficiarios del Proyecto

Los beneficiarios del proyecto incluyen inversionistas, analistas financieros, investigadores académicos y organizaciones relacionadas con los sectores financiero y tecnológico interesadas en el análisis predictivo del mercado bursátil.

El proyecto se desarrolla dentro del dominio de las finanzas computacionales aplicadas al mercado de valores.

## Alcance del Proyecto

### Incluye

Los datos disponibles para el desarrollo del proyecto consisten en información histórica de la acción de Tesla obtenida a través de plataformas financieras como Yahoo Finance mediante herramientas de extracción de datos basadas en Python.

El conjunto de datos incluye variables financieras diarias como:

* Open (Precio de apertura)
* High (Precio máximo)
* Low (Precio mínimo)
* Close (Precio de cierre)
* Volume (Volumen de negociación)

Estas variables corresponden al período comprendido entre los años 2015 y 2025.

Adicionalmente, se incorporarán indicadores técnicos derivados como:

* RSI (Relative Strength Index)
* MACD (Moving Average Convergence Divergence)
* Medias móviles (Moving Averages)
* Bandas de Bollinger (Bollinger Bands)

con el propósito de enriquecer el análisis de series temporales y proporcionar información relevante al modelo de Deep Learning.

Los criterios de éxito del proyecto se centrarán en evaluar tanto el desempeño predictivo como la capacidad de generalización del modelo sobre datos no vistos previamente.

Para ello se utilizarán métricas de evaluación como:

* Accuracy
* Precision
* Recall
* F1-Score

### Alcance Específico

**PT1.1 — Predicción de la Dirección Subida/Bajada mediante LSTM**

## Metodología

Los resultados esperados del proyecto consisten en desarrollar un modelo LSTM capaz de identificar patrones en el comportamiento histórico de las acciones de Tesla y predecir la dirección futura del precio de la acción, específicamente si el valor tenderá a subir o bajar durante el siguiente período de negociación.

Se espera que el modelo aproveche las capacidades de las redes neuronales convolucionales para detectar patrones locales y de las redes LSTM para modelar dependencias temporales de largo plazo, permitiendo generar predicciones más robustas y útiles para el análisis financiero.
