[Volver al README](../../../../README.md)

##Objetivo General
Diseñar, entrenar y desplegar un modelo de aprendizaje profundo que permita predecir la dirección del precio de cierre de la acción de Tesla utilizando datos históricos de mercado.

## Adquisición de Datos

Se recopilan datos históricos de Tesla incluyendo variables fundamentales del mercado:

Open
High
Low
Close
Volume

# Se generan variables derivadas y etiquetas binarias que representan la dirección futura del mercado:

1: el precio sube.
0: el precio baja o permanece estable.
s
# Construccion de secuencias de tiempo:

Los datos son transformados en ventanas temporales utilizando diferentes valores de Sequence Length:

5 días
10 días
15 días
20 días
30 días

# Entrenamiento

Se evaluaron diferentes arquitecturas de redes neuronales.active
