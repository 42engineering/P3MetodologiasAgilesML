[Volver al README](../../../../README.md)

# Exit Report – Sistema de Predicción de Movimiento Bursátil de Tesla (TSLA)

## 1. Resumen Ejecutivo

El presente proyecto tuvo como objetivo desarrollar una solución de aprendizaje automático capaz de predecir la dirección del movimiento del precio de la acción de Tesla (TSLA) utilizando información histórica del mercado bursátil. Para ello se implementó un pipeline completo de Machine Learning que incluyó adquisición de datos, preprocesamiento, entrenamiento, evaluación y despliegue de modelos de Deep Learning.

Durante la fase de modelación se evaluaron múltiples arquitecturas basadas en redes neuronales recurrentes y convolucionales, incluyendo LSTM, LSTM1, DeepLSTM1, CNNLSTM1 y DeepLSTM1 enriquecido con indicadores técnicos. Los resultados permitieron seleccionar CNNLSTM1 y DeepLSTM1_Indicadores1 como las arquitecturas con mejor desempeño general.

El proyecto concluyó exitosamente con la implementación de una solución desplegada que permite realizar predicciones en tiempo real mediante una interfaz web conectada a una API REST desarrollada con FastAPI.

---

## 2. Objetivos del Proyecto

### Objetivo General

Desarrollar un sistema de predicción bursátil basado en Deep Learning capaz de estimar la dirección futura del movimiento de la acción de Tesla utilizando información histórica del mercado.

### Objetivos Específicos

* Obtener y preparar datos históricos de Tesla.
* Construir modelos de Deep Learning para series temporales.
* Comparar diferentes arquitecturas y ventanas temporales.
* Seleccionar los modelos con mejor desempeño.
* Implementar una API para realizar inferencias.
* Desplegar una solución accesible mediante una interfaz web.

---

## 3. Entregables Generados

### Código Fuente

* Pipeline de adquisición de datos.
* Pipeline de preprocesamiento.
* Pipeline de entrenamiento.
* Pipeline de evaluación.
* API REST con FastAPI.
* Frontend desarrollado con HTML, CSS y JavaScript.

### Modelos Entrenados

* LSTM
* LSTM1
* DeepLSTM1
* CNNLSTM1
* DeepLSTM1_Indicadores1

### Artefactos Generados

* Modelos en formato `.keras`.
* Escaladores MinMaxScaler.
* Archivos de comparación de métricas.
* Gráficos de entrenamiento.
* Documentación técnica y funcional.

### Documentación
[Ver documentacion en archivo README ](../../../../README.md)

---

## 4. Resultados de la Modelación

Se evaluaron múltiples configuraciones utilizando secuencias temporales de 5, 10, 15, 20 y 30 días.

Los resultados mostraron que:

* CNNLSTM1 obtuvo uno de los mejores desempeños generales gracias a la combinación de capas convolucionales y LSTM.
* DeepLSTM1_Indicadores1 logró resultados competitivos al incorporar indicadores técnicos financieros.
* Las métricas Accuracy y F1-Score presentaron mejoras respecto al modelo baseline.
* Las métricas AUC se mantuvieron cercanas a 0.50, reflejando la complejidad inherente de la predicción bursátil.

Los modelos seleccionados como mejores alternativas fueron:

| Modelo                 | Característica principal               |
| ---------------------- | -------------------------------------- |
| CNNLSTM1               | Arquitectura híbrida CNN + LSTM        |
| DeepLSTM1_Indicadores1 | LSTM profunda con indicadores técnicos |

---

## 5. Despliegue de la Solución

### Arquitectura Implementada

```text
Usuario
   ↓
Frontend FE_TSLA_V1_0 (Vercel)
   ↓
FastAPI REST API (Render)
   ↓
TensorFlow Runtime
   ↓
Modelo seleccionado
   ↓
Predicción TSLA
```

### Frontend

El frontend fue desplegado utilizando Vercel y permite:

* Seleccionar una fecha de predicción.
* Seleccionar el modelo a utilizar.
* Consultar la API de predicción.
* Visualizar los resultados obtenidos.

### Backend

El backend fue desarrollado utilizando FastAPI y desplegado en Render.

Endpoints implementados:

| Endpoint       | Función                      |
| -------------- | ---------------------------- |
| /health        | Estado de la API             |
| /models        | Lista de modelos disponibles |
| /predict       | Generación de predicciones   |
| /latest-window | Consulta de datos recientes  |

### Modelos Disponibles en Producción

* LSTM
* LSTM1
* DeepLSTM1
* CNNLSTM1

Los modelos DeepLSTM1_Indicadores1 fueron entrenados exitosamente, pero no fueron incluidos en el despliegue final debido a dependencias adicionales asociadas al cálculo de indicadores técnicos.

---

## 6. Problemas Encontrados

Durante el despliegue se identificaron varios desafíos técnicos:

### Compatibilidad de Dependencias

La librería pandas_ta utilizada para generar indicadores técnicos presentó problemas de compatibilidad entre el entorno de entrenamiento y el entorno de producción.

La versión utilizada durante el entrenamiento no pudo instalarse correctamente en Render, impidiendo la reconstrucción automática de indicadores técnicos durante la inferencia.

---

## 7. Lecciones Aprendidas

* La reproducibilidad del entorno es un factor crítico en proyectos de Machine Learning.

---

## 8. Oportunidades de Mejora

Se identifican las siguientes oportunidades para futuras versiones:

* Incorporar datos macroeconómicos y noticias financieras.
* Implementar análisis de sentimiento.
* Automatizar el reentrenamiento periódico de modelos.
* Incorporar monitoreo de desempeño en producción.
* Desarrollar una implementación propia de indicadores técnicos utilizando Pandas y NumPy para eliminar dependencias externas.
* Explorar arquitecturas basadas en Transformers para series temporales.

---

## 9. Estado Final del Proyecto

| Componente               | Estado     |
| ------------------------ | ---------- |
| Adquisición de datos     | Completado |
| Preprocesamiento         | Completado |
| Entrenamiento de modelos | Completado |
| Evaluación de modelos    | Completado |
| API REST                 | Completado |
| Frontend Web             | Completado |
| Despliegue Backend       | Completado |
| Despliegue Frontend      | Completado |
| Documentación            | Completado |

Para mayor infomacion detallada ver [archivo README](../../README.md)

---

## 10. Conclusión de Cierre

El proyecto logró cumplir satisfactoriamente los objetivos planteados al inicio del desarrollo. Se construyó una solución funcional para la predicción de movimientos bursátiles utilizando técnicas de Deep Learning, integrando procesos de adquisición de datos, modelación, evaluación y despliegue en un entorno accesible para usuarios finales.

