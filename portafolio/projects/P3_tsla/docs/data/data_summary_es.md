[Volver al README](../../../../README.md)

# Resumen general de los datos

El conjunto de datos utilizado corresponde al histórico financiero de la acción de Tesla (TSLA), obtenido mediante la librería `yfinance`. Las variables originales incluyen información diaria de precios bursátiles y volumen de transacciones.

El dataset contiene variables numéricas continuas relacionadas con el comportamiento del mercado:

* Open
* High
* Low
* Close
* Volume

Posteriormente, se generó una variable objetivo llamada `SubeBaja`, la cual representa la dirección esperada del precio de cierre para el siguiente día bursátil:

* `1`: el precio subirá.
* `0`: el precio bajará o no subirá.

El pipeline realiza un preprocesamiento orientado a modelos de series temporales, utilizando secuencias de longitud fija para alimentar las redes neuronales LSTM. Para ello:

* Se eliminaron valores faltantes y duplicados.
* Se normalizaron las variables utilizando `MinMaxScaler`.
* Se construyeron ventanas temporales de 30 y 60 periodos.
* Los datos fueron divididos en conjuntos de entrenamiento y prueba manteniendo el orden temporal (`shuffle=False`).

Adicionalmente, se realizaron visualizaciones de series de tiempo, histogramas y gráficos de densidad para comprender el comportamiento de las variables financieras.

---

# Resumen de calidad de los datos

Durante la etapa de análisis exploratorio se evaluó la calidad de los datos considerando valores faltantes, duplicados y comportamiento estadístico de las variables.

## Valores faltantes

Se verificó la presencia de valores nulos mediante:

```python
df.isnull().sum()
```

Los registros con valores faltantes fueron eliminados utilizando:

```python
df.dropna(inplace=True)
```

Esto permitió garantizar la integridad de las secuencias temporales utilizadas por el modelo.

## Valores duplicados

Se identificaron registros duplicados mediante:

```python
df.duplicated().sum()
```

Los duplicados encontrados fueron removidos utilizando:

```python
df.drop_duplicates(inplace=True)
```

## Valores extremos y comportamiento estadístico

Debido a la naturaleza financiera de los datos, las variables presentan:

* Alta volatilidad.
* Distribuciones no gaussianas.
* Colas pesadas.
* Volatilidad agrupada.

Estas características son comunes en series financieras y fueron evidenciadas mediante histogramas y gráficos de densidad.

## Transformaciones aplicadas

Para mejorar el entrenamiento de las redes neuronales LSTM, las variables fueron normalizadas entre 0 y 1 mediante `MinMaxScaler`:

```python
scaler = MinMaxScaler(feature_range=(0,1))
```

La normalización ayuda a estabilizar el entrenamiento y acelerar la convergencia del modelo.

---

# Variable objetivo

La variable objetivo del proyecto es `SubeBaja`, construida a partir del precio de cierre (`Close`) de Tesla.

La variable fue generada utilizando la siguiente lógica:

```python
data['SubeBaja'] = np.where(
    data['Close'].shift(-1) > data['Close'],
    1,
    0
)
```

Interpretación:

* `1`: el precio de cierre del siguiente día es mayor al actual.
* `0`: el precio disminuye o permanece igual.

El problema se plantea como una tarea de clasificación binaria.

## Distribución de la variable objetivo

La distribución de clases fue analizada utilizando gráficos de barras. Los resultados muestran una distribución relativamente balanceada entre las clases 0 y 1, lo cual favorece el entrenamiento del modelo y reduce el riesgo de sesgo hacia una clase dominante.

La visualización se realizó mediante la función:

```python
plotBatchTargetDistribution(y)
```

---

# Variables individuales

## Open

Representa el precio de apertura diario de la acción de Tesla. Esta variable permite identificar el valor inicial del activo en cada sesión bursátil.

Se analizaron estadísticas descriptivas como:

* Media
* Desviación estándar
* Valores mínimos y máximos

## High

Corresponde al precio máximo alcanzado por la acción durante la jornada bursátil. Permite analizar la volatilidad intradía.

## Low

Representa el precio mínimo registrado durante la sesión bursátil. Junto con `High`, ayuda a medir el rango de fluctuación diaria.

## Close

Es una de las variables más importantes del análisis, ya que se utiliza para generar la variable objetivo. Se realizaron:

* Series de tiempo.
* Histogramas.
* Gráficos de densidad.

Los análisis mostraron concentración de precios en determinados rangos y presencia de alta volatilidad.

## Volume

Representa el número de acciones transadas diariamente. Esta variable permite identificar cambios importantes en la actividad del mercado y posibles eventos financieros relevantes.

Se observaron:

* Distribuciones altamente asimétricas.
* Presencia de picos de actividad bursátil.

## Transformaciones aplicadas

Todas las variables financieras fueron normalizadas utilizando `MinMaxScaler` para asegurar que compartieran una escala homogénea durante el entrenamiento de la red neuronal.

---

# Ranking de variables

El pipeline no implementa explícitamente técnicas de selección automática de variables como PCA o importancia basada en árboles. Sin embargo, las variables utilizadas fueron seleccionadas por su relevancia financiera y temporal.

Las variables más importantes para el modelo son:

1. Close
2. Volume
3. High
4. Low
5. Open

La variable `Close` tiene la mayor relevancia debido a que la variable objetivo depende directamente de la evolución temporal del precio de cierre.
Adicionalmente, las redes LSTM aprenden relaciones temporales complejas entre las variables financieras, por lo que la importancia de cada variable se modela implícitamente durante el entrenamiento.


## Relaciones entre variables financieras

Las variables `Open`, `High`, `Low` y `Close` presentan alta correlación debido a que todas describen el comportamiento diario del precio bursátil.

Estas relaciones fueron analizadas mediante:

* Gráficos de series temporales.
* Histogramas.
* Gráficos de densidad.

## Modelado temporal

El modelo LSTM captura dependencias temporales entre las variables explicativas y la variable objetivo utilizando secuencias históricas de precios y volumen.
Esto permite aprender patrones secuenciales complejos presentes en los datos financieros y generar predicciones sobre la dirección futura del precio de Tesla.

## Modelos seleccionados

Para el proyecto se utilizaron modelos de redes neuronales LSTM (Long Short-Term Memory), debido a su capacidad para trabajar con series de tiempo financieras y aprender patrones temporales en los precios de las acciones. Se implementó un modelo SimpleLSTM, compuesto por una capa LSTM y una capa densa de salida, utilizado como modelo base para la clasificación binaria de la dirección del precio de Tesla.

También se implementó el modelo DeepLSTM1, una arquitectura más profunda con múltiples capas LSTM y capas Dropout para reducir el sobreajuste. Este modelo fue optimizado utilizando EarlyStopping, permitiendo mejorar el rendimiento y detener el entrenamiento cuando la pérdida de validación dejaba de mejorar. Ambos modelos fueron evaluados mediante métricas de accuracy, matriz de confusión y classification report.

[Volver al README](../README.md)