# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

El proyecto propone el desarrollo de un modelo híbrido de Deep Learning basado en arquitecturas CNN-LSTM para la predicción del comportamiento de las acciones de TSLA utilizando exclusivamente datos históricos del mercado e indicadores técnicos.

## Objetivo del Proyecto

Los beneficiarios del proyecto son inversionistas, analistas financieros, investigadores académicos y organizaciones relacionadas con el sector financiero y tecnológico interesados en el análisis predictivo de mercados bursátiles.

El proyecto se desarrolla dentro del dominio de las finanzas computacionales aplicado a mercado de valores.

## Alcance del Proyecto

### Incluye:

Los datos disponibles para el desarrollo del proyecto corresponden a información histórica bursátil de TSLA obtenida desde plataformas financieras como Yahoo Finance mediante herramientas de extracción de datos en Python. El conjunto de datos incluye variables financieras diarias como Open, High, Low, Close y Volume (OHLCV) para el periodo comprendido entre 2015 y 2025. Además, se incorporarán indicadores técnicos derivados, tales como RSI, MACD, medias móviles y bandas de Bollinger, con el fin de enriquecer el análisis de las series temporales y proporcionar información relevante al modelo de Deep Learning.

Los criterios de éxito del proyecto estarán enfocados en evaluar tanto el desempeño predictivo como la capacidad de generalización del modelo sobre datos no vistos. Para ello, se utilizarán métricas de evaluación como Accuracy, Precision, Recall y F1-Score. 

## Metodología

Los resultados esperados del proyecto consisten en el desarrollo de un modelo híbrido CNN-LSTM capaz de identificar patrones  en el comportamiento histórico de las acciones de Tesla y predecir la dirección futura del precio de la acción, específicamente si el valor tenderá a subir o bajar en el siguiente periodo bursátil. Se espera que el modelo aproveche las capacidades de las redes convolucionales para detectar patrones locales y de las redes LSTM para modelar dependencias temporales de largo plazo, permitiendo obtener predicciones más robustas y útiles para el análisis financiero.

## Cronograma

| Etapa                                                                                            | Duración Estimada | Fechas                       |
| ------------------------------------------------------------------------------------------------ | ----------------- | ---------------------------- |
| Entendimiento del negocio y carga de datos históricos de TSLA                                    | 1 semana          | del 1 de mayo al 7 de mayo   |
| Preprocesamiento y análisis exploratorio de datos financieros                                    | 1 semana          | del 8 de mayo al 14 de mayo  |
| Modelamiento y extracción de características mediante indicadores técnicos y ventanas temporales | 1 semana          | del 15 de mayo al 21 de mayo |
| Despliegue del modelo CNN-LSTM y pruebas de predicción                                           | 1 semana          | del 22 de mayo al 28 de mayo |
| Evaluación del modelo, backtesting financiero y entrega final                                    | 1 semana          | del 29 de mayo al 4 de junio |


