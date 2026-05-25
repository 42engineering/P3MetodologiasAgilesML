#Librerias Fase1
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import yfinance as yf

df = yf.download(
    "TSLA",
    start="2015-01-01",
    end="2025-12-31"
)

print(df.head())



