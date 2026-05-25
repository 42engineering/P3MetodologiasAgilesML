[Volver al README](../../../../README.md)

# Diccionario de datos

## Base de datos 1

| Variable | Descripción                                                              | Tipo de dato | Rango/Valores posibles                         | Fuente de datos            |
| -------- | ------------------------------------------------------------------------ | ------------ | ---------------------------------------------- | -------------------------- |
| Open     | Precio de apertura de la acción de Tesla al inicio de la sesión bursátil | float        | Valores positivos en USD (`Open > 0`)          | Yahoo Finance (`yfinance`) |
| High     | Precio máximo alcanzado por la acción durante la sesión bursátil         | float        | Valores positivos en USD (`High ≥ Open/Close`) | Yahoo Finance (`yfinance`) |
| Low      | Precio mínimo alcanzado por la acción durante la sesión bursátil         | float        | Valores positivos en USD (`Low ≤ Open/Close`)  | Yahoo Finance (`yfinance`) |
| Close    | Precio de cierre de la acción al final de la sesión bursátil             | float        | Valores positivos en USD (`Close > 0`)         | Yahoo Finance (`yfinance`) |
| Volume   | Cantidad de acciones transadas durante la sesión bursátil                | integer      | Valores enteros positivos (`Volume ≥ 0`)       | Yahoo Finance (`yfinance`) |
| Sube/Baja  | Direccion esperada de la accion                                        | boolean      | el precio subirá (`1`) o bajará/no subirá (`0`)| modelo      |
-----


- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.

 