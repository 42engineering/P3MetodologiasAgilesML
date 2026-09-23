[Back to README](/portafolio/projects/P3_tsla/README.md)

# (Project Charter) – Business Understanding

## Project Name

Financial Direction Prediction for TSLA Using Neural Networks

## Project Objective

The project proposes the development of a hybrid Deep Learning model based on LSTM architectures to predict the behavior of Tesla (TSLA) stock, using exclusively historical market data and financial technical indicators.

## Project Beneficiaries

The beneficiaries of the project include investors, financial analysts, academic researchers, and organizations related to the financial and technology sectors interested in predictive stock market analysis.

The project is developed within the domain of computational finance applied to the stock market.

## Project Scope

### Includes

The data available for the development of the project consists of historical Tesla stock information obtained through financial platforms such as Yahoo Finance using Python-based data extraction tools.

The dataset includes daily financial variables such as:

* Open (Opening Price)
* High (Highest Price)\
* Low (Lowest Price)
* Close (Closing Price)
* Volume (Trading Volume)

These variables correspond to the period between 2015 and 2025.
Additionally, derived technical indicators will be incorporated, such as:

* RSI (Relative Strength Index)
* MACD (Moving Average Convergence Divergence)
* Moving Averages
* Bollinger Bands

with the purpose of enriching the time-series analysis and providing relevant information to the Deep Learning model.

The project success criteria will focus on evaluating both the predictive performance and the model's ability to generalize to previously unseen data.

The following evaluation metrics will be used:

* Accuracy
* Precision
* Recall
* F1-Score

### Specific Scope

**PT1.1 — Up/Down Direction Prediction Using LSTM**

## Methodology

The expected outcome of the project is to develop an LSTM model capable of identifying patterns in Tesla stock's historical behavior and predicting the future direction of the stock price, specifically whether the value is expected to rise or fall during the next trading period.

The model is expected to leverage the capabilities of convolutional neural networks to detect local patterns and LSTM networks to model long-term temporal dependencies, enabling more robust and useful predictions for financial analysis.
