[Volver al README](../../../../README.md)

# Reporte del Modelo Final

## Resumen Ejecutivo

Durante la fase de modelado se evaluaron diversas arquitecturas de redes neuronales recurrentes, incluyendo modelos LSTM, LSTM1, DeepLSTM1, CNNLSTM1 y DeepLSTM1 enriquecido con indicadores técnicos financieros. 

## Descripción del Problema

La predicción de movimientos bursatiles constituye uno de los problemas más complejos dentro del ana`lisis financiero debido a la naturaleza dina`mica, no lineal y altamente volatil de los mercados.

En este proyecto se abordó el problema de clasificación binaria del movimiento diario de la acción de Tesla (TSLA), donde el objetivo consiste en determinar si el precio de cierre presentara` una variación positiva o negativa a partir de información histórica del mercado.

## Descripción del Modelo

| Modelo                     | Descripción                                                                          | Capas principales                                                |
| -------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **LSTM (Baseline)**        | Modelo recurrente básico utilizado como línea base de comparación.                   | LSTM → Dense → Dense                                             |
| **LSTM1**                  | Versión mejorada del modelo baseline con mayor capacidad de aprendizaje.             | LSTM → Dropout → Dense → Dense                                   |
| **DeepLSTM1**              | Arquitectura profunda para capturar patrones temporales más complejos.               | LSTM → Dropout → LSTM → Dropout → LSTM → Dropout → Dense → Dense |
| **CNNLSTM1**               | Modelo híbrido que combina extracción de patrones locales y dependencias temporales. | Conv1D → MaxPooling1D → LSTM → Dense → Dense                     |
| **DeepLSTM1_INDICADORES1** | DeepLSTM1 enriquecido con indicadores técnicos financieros.                          | LSTM → Dropout → LSTM → Dropout → LSTM → Dropout → Dense → Dense |

# Modelo CNNLSTM1

CNNLSTM1 es una arquitectura híbrida que combina redes convolucionales unidimensionales (CNN) con redes neuronales recurrentes LSTM.
La capa convolucional permite detectar patrones locales y tendencias de corto plazo presentes en las secuencias temporales, mientras que la capa LSTM modela dependencias temporales de largo plazo.

# DeepLSTM1_Indicadores1

 Este modelo cuenta con una arquitectura LSTM profunda que incorpora indicadores técnicos financieros (RSI, MACD, ATR y EMA) junto con variables OHLCV para mejorar la identificación de patrones temporales y tendencias del mercado bursátil. Junto con el conjunto de variables financieras OHLCV (Open, High, Low, Close, Volumne).active

# Ventanas temporales
 Se utilizaron ventanas temprales de [5,10,15,20, 30] dias.

## Evaluación del Modelo

Los resultados obtenidos permitieron identificar dos modelos con el mejor desempeño general: CNNLSTM1 y DeepLSTM1_Indicadores1.
Para evaluar el desempeño de los modelos se utilizaron las siguientes métricas:

Accuracy
Precision
Recall
F1-Score
AUC-ROC
Binary Cross Entropy Loss

En el caso del modelo CNNLSTM1, la mejor configuración correspondió a una secuencia de 15 días, alcanzando una exactitud (Accuracy) de 0.5127 y un F1-Score de 0.6779. Estos resultados indican que la combinación de capas convolucionales y LSTM permitió capturar patrones locales y temporales relevantes dentro de la serie financiera, obteniendo el mejor desempeño entre las configuraciones evaluadas para esta arquitectura.

Por su parte, el modelo DeepLSTM1_Indicadores1 incorporó indicadores técnicos financieros como RSI, MACD, ATR y EMA con el objetivo de enriquecer la información disponible para el aprendizaje. La mejor configuración fue obtenida con una ventana temporal de 5 días, alcanzando una exactitud de 0.5128 y un F1-Score de 0.6780. Aunque la mejora respecto a otras configuraciones fue moderada, los resultados sugieren que la incorporación de indicadores técnicos aporta información complementaria útil para el proceso de predicción.

Se pueden ver mas detalles sobre la modelacione en el archivo:

- [Notebook1](/tdsp_template/P3_tsla/scripts/data_acquisition/PT1.1ColabV2.ipynb) - Notebook implementation model

## Conclusiones y Recomendaciones

Las métricas AUC se mantuvieron cercanas a 0.50 en la mayoría de los experimentos, evidenciando la complejidad de predecir movimientos bursátiles y la alta volatilidad del mercado. Este comportamiento refleja la influencia de factores externos que no están incluidos en los datos históricos utilizados.

En conclusión, CNNLSTM1 y DeepLSTM1_Indicadores1 fueron seleccionados como los modelos finales del proyecto. CNNLSTM1 destacó por combinar capas convolucionales y LSTM para capturar patrones temporales, mientras que DeepLSTM1_Indicadores1 mostró el beneficio de incorporar indicadores técnicos financieros. Ambos modelos representan una base sólida para futuras mejoras.active

- La senal de entrenamiento es baja aun usando Indicadores financieros,  es posible incorporar nuevas fuentes de información, tales como indicadores macroeconómicos, sentimiento de noticias financieras o variables derivadas de redes sociales, con el objetivo de enriquecer la capacidad predictiva de los modelos.

- Es posible mejorar la interfase de usuario para incluir las graficas del mercado y los datos en tiempo real para realizar las predicciones.


## Referencias

* Yahoo Finance (`yfinance`) – Fuente de datos financieros históricos de Tesla.
* TensorFlow/Keras – Implementación de redes neuronales LSTM.
* Scikit-learn – Preprocesamiento, normalización y métricas de evaluación.
* MLflow – Seguimiento y registro de experimentos de machine learning.
