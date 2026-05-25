[Back to README](../../../../README.md)

# Project Charter - Business Understanding

## Project Name
TSLA Financial Direction Prediction Using Neural Networks

## Project Objective
The project proposes the development of a hybrid Deep Learning model based on LSTM architectures for predicting TSLA stock behavior using exclusively historical market data and technical indicators.

## Project Beneficiaries

The beneficiaries of the project include investors, financial analysts, academic researchers, and organizations related to the financial and technology sectors interested in predictive stock market analysis.

The project is developed within the domain of computational finance applied to the stock market.

## Project Scope

### Includes:

The data available for the development of the project consists of historical TSLA stock market information obtained from financial platforms such as Yahoo Finance through Python-based data extraction tools. The dataset includes daily financial variables such as Open, High, Low, Close, and Volume (OHLCV) for the period between 2015 and 2025. Additionally, derived technical indicators such as RSI, MACD, moving averages, and Bollinger Bands will be incorporated to enrich the time series analysis and provide relevant information to the Deep Learning model.

The project success criteria will focus on evaluating both predictive performance and the model’s generalization capability on unseen data. For this purpose, evaluation metrics such as Accuracy, Precision, Recall, and F1-Score will be used.

### Specific Scope

PT1.1 — Up/Down Direction Prediction Using LSTM

## Methodology

The expected results of the project consist of developing an LSTM model capable of identifying patterns in the historical behavior of Tesla stocks and predicting the future direction of the stock price, specifically whether the value will tend to rise or fall in the next trading period. The model is expected to leverage the capabilities of convolutional neural networks to detect local patterns and LSTM networks to model long-term temporal dependencies, enabling more robust and useful predictions for financial analysis.

## Timeline

| Stage                                                                                            | Estimated Duration | Dates                        |
| ------------------------------------------------------------------------------------------------ | ------------------ | ---------------------------- |
| Business understanding and loading of historical TSLA data                                       | 1 week             | May 1 to May 7               |
| Preprocessing and exploratory analysis of financial data                                         | 1 week             | May 8 to May 14              |
| Modeling and feature extraction using technical indicators and temporal windows                  | 1 week             | May 15 to May 21             |
| CNN-LSTM model deployment and prediction testing                                                 | 1 week             | May 22 to May 28             |
| Model evaluation, financial backtesting, and final delivery                                      | 1 week             | May 29 to June 4             |