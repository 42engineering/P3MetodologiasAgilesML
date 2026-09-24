[Back to README](/portafolio/projects/P3_tsla/README.md)

# Final Model Report

## Executive Summary

During the modeling phase, several recurrent neural network architectures were evaluated, including LSTM, LSTM1, DeepLSTM1, CNNLSTM1, and DeepLSTM1 enhanced with financial technical indicators.

## Problem Description

Stock market movement prediction is one of the most complex problems in financial analysis due to the dynamic, nonlinear, and highly volatile nature of financial markets.

This project addressed the binary classification problem of Tesla (TSLA) daily stock movement, where the objective is to determine whether the closing price will show a positive or negative variation based on historical market information.

## Model Description

| Model                      | Description                                                                | Main Layers                                                      |
| -------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **LSTM (Baseline)**        | Basic recurrent model used as the comparison baseline.                     | LSTM → Dense → Dense                                             |
| **LSTM1**                  | Improved version of the baseline model with greater learning capacity.     | LSTM → Dropout → Dense → Dense                                   |
| **DeepLSTM1**              | Deep architecture designed to capture more complex temporal patterns.      | LSTM → Dropout → LSTM → Dropout → LSTM → Dropout → Dense → Dense |
| **CNNLSTM1**               | Hybrid model combining local pattern extraction and temporal dependencies. | Conv1D → MaxPooling1D → LSTM → Dense → Dense                     |
| **DeepLSTM1_INDICADORES1** | DeepLSTM1 enhanced with financial technical indicators.                    | LSTM → Dropout → LSTM → Dropout → LSTM → Dropout → Dense → Dense |

# CNNLSTM1 Model

CNNLSTM1 is a hybrid architecture that combines one-dimensional convolutional neural networks (CNN) with recurrent LSTM neural networks.

The convolutional layer detects local patterns and short-term tren ds within temporal sequences, while the LSTM layer models long-term temporal dependencies.

# DeepLSTM1_Indicadores1

This model uses a deep LSTM architecture that incorporates financial technical indicators (RSI, MACD, ATR, and EMA) together with OHLCV variables to improve the identification of temporal patterns and stock market trends.

These indicators are combined wit
