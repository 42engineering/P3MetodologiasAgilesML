[Back to README](/portafolio/projects/P3_tsla/README.md)

# Data Overview

The dataset used in this project corresponds to Tesla (TSLA) historical financial data obtained through the `yfinance` library. The original variables include daily stock price and trading volume information.

The dataset contains continuous numerical variables related to market behavior:

* Open
* High
* Low\
* Close
* Volume

A target variable called `SubeBaja` was subsequently created. This variable represents the expected direction of the closing price for the next trading day:

* `1`: the price will increase.
* `0`: the price will decrease or will not increase.

The pipeline performs preprocessing designed for time-series models by using fixed-length sequences as input to the LSTM neural networks. The following steps were performed:

* Missing values and duplicates were removed.
* Variables were normalized using `MinMaxScaler`.
* Time windows of 30 and 60 periods were created.
* The data was split into training and test sets while preserving temporal order (`shuffle=False`).

Additionally, time-series plots, histograms, and density plots were generated to better understand the behavior of the financial variables.

---

# Data Quality Overview

During the exploratory data analysis stage, data quality was evaluated by considering missing values, duplicates, and the statistical behavior of the variables.

