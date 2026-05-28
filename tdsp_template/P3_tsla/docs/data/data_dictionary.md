[Volver al README](../../../../README.md)

# Diccionario de datos

| Variable                 | Descripción                                                                                | Tipo de dato      | Rango/Valores posibles                                | Fuente de datos                    |
| ------------------------ | ------------------------------------------------------------------------------------------ | ----------------- | ----------------------------------------------------- | ---------------------------------- |
| Open                     | Precio de apertura de la acción de Tesla al inicio de la sesión bursátil                   | float             | Valores positivos en USD (`Open > 0`)                 | Yahoo Finance (`yfinance`)         |
| High                     | Precio máximo alcanzado por la acción durante la sesión bursátil                           | float             | Valores positivos en USD (`High ≥ Open/Close`)        | Yahoo Finance (`yfinance`)         |
| Low                      | Precio mínimo alcanzado por la acción durante la sesión bursátil                           | float             | Valores positivos en USD (`Low ≤ Open/Close`)         | Yahoo Finance (`yfinance`)         |
| Close                    | Precio de cierre de la acción al final de la sesión bursátil                               | float             | Valores positivos en USD (`Close > 0`)                | Yahoo Finance (`yfinance`)         |
| Volume                   | Cantidad de acciones transadas durante la sesión bursátil                                  | integer           | Valores enteros positivos (`Volume ≥ 0`)              | Yahoo Finance (`yfinance`)         |
| SubeBaja                 | Variable objetivo que indica si el precio de cierre del siguiente día será mayor al actual | boolean / integer | `1 = el precio sube`, `0 = el precio baja o no sube`  | Generada mediante preprocesamiento |
| caracteristicasEscaladas | Variables financieras escaladas usando normalización Min-Max                               | array de float    | Valores entre `0` y `1`                               | Transformación con `MinMaxScaler`  |
| X                        | Secuencias temporales utilizadas como entrada para la red LSTM                             | array 3D          | Secuencias de longitud `30` con variables financieras | Generadas en el pipeline           |
| y                        | Etiquetas objetivo asociadas a cada secuencia temporal                                     | array integer     | `0` o `1`                                             | Generadas a partir de `SubeBaja`   |
| XTrain                   | Conjunto de entrenamiento de secuencias temporales                                         | array 3D          | Datos normalizados para entrenamiento                 | División con `train_test_split`    |
| XTest                    | Conjunto de prueba de secuencias temporales                                                | array 3D          | Datos normalizados para evaluación                    | División con `train_test_split`    |
| yTrain                   | Etiquetas del conjunto de entrenamiento                                                    | array integer     | `0` o `1`                                             | División con `train_test_split`    |
| yTest                    | Etiquetas del conjunto de prueba                                                           | array integer     | `0` o `1`                                             | División con `train_test_split`    |
| yPredProb                | Probabilidades predichas por el modelo LSTM                                                | float             | Valores entre `0` y `1`                               | Salida del modelo                  |
| yPred                    | Predicción binaria final del modelo                                                        | integer           | `1 = subida`, `0 = bajada/no subida`                  | Salida procesada del modelo        |
| Accuracy                 | Métrica de precisión del modelo                                                            | float             | Valores entre `0` y `1`                               | Evaluación del modelo              |
| Loss                     | Error calculado mediante entropía cruzada binaria                                          | float             | Valores positivos (`Loss ≥ 0`)                        | Evaluación del modelo              |
| sequenceLength           | Número de pasos temporales utilizados por cada secuencia de entrada                        | integer           | Valor fijo (`30` o `60`)                              | Configuración del pipeline         |
| epochNumber              | Número de épocas utilizadas durante el entrenamiento                                       | integer           | Valores enteros positivos                             | Configuración del entrenamiento    |
| batch_size               | Cantidad de muestras procesadas por iteración de entrenamiento                             | integer           | Valores enteros positivos                             | Configuración del entrenamiento    |


- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.

 