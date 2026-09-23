[Back to README](/portafolio/projects/P3_tsla/README.md)

**# Exit Report – Tesla (TSLA) Stock Movement Prediction System**

**## 1. Executive Summary**

The objective of this project was to develop a Machine Learning solution capable of predicting the direction of Tesla (TSLA) stock price movements using historical stock market data. To achieve this, a complete Machine Learning pipeline was implemented, including data acquisition, preprocessing, training, evaluation, and deployment of Deep Learning models.

During the modeling phase, multiple architectures based on recurrent and convolutional neural networks were evaluated, including LSTM, LSTM1, DeepLSTM1, CNNLSTM1, and DeepLSTM1 enhanced with technical indicators. The results led to the selection of CNNLSTM1 and DeepLSTM1_Indicadores1 as the architectures with the best overall performance.

The project was successfully completed with the implementation of a deployed solution that enables real-time predictions through a web interface connected to a REST API developed with FastAPI.

**---**

**## 2. Project Objectives**

**### General Objective**

Develop a Deep Learning-based stock market prediction system capable of estimating the future direction of Tesla stock movements using historical market data.

**### Specific Objectives**

* Obtain and prepare historical Tesla data.

* Build Deep Learning models for time series.

* Compare different architectures and time windows.

* Select the best-performing models.

* Implement an API for inference.

* Deploy a solution accessible through a web interface.

**---**

**## 3. Deliverables Generated**

**### Source Code**

* Data acquisition pipeline.

* Preprocessing pipeline.

* Training pipeline.

* Evaluation pipeline.

* REST API with FastAPI.

* Frontend developed with HTML, CSS, and JavaScript.

**### Trained Models**

* LSTM

* LSTM1

* DeepLSTM1

* CNNLSTM1

* DeepLSTM1_Indicadores1

**### Generated Artifacts**

* Models in `.keras` format.

* MinMaxScaler scalers.

* Metric comparison files.

* Training plots.

* Technical and functional documentation.

**### Documentation**

[View documentation in the README file](../../../../README.md)

**---**

**## 4. Modeling Results**

Multiple configurations were evaluated using time sequences of 5, 10, 15, 20, and 30 days.

The results showed that:

* CNNLSTM1 achieved one of the best overall performances due to the combination of convolutional and LSTM layers.

* DeepLSTM1_Indicadores1 achieved competitive results by incorporating financial technical indicators.

* Accuracy and F1-Score metrics showed improvements compared to the baseline model.

* AUC metrics remained close to 0.50, reflecting the inherent complexity of stock market prediction.

The models selected as the best alternatives were:

| Model                  | Main Feature                        |
| ---------------------- | ----------------------------------- |
| CNNLSTM1               | Hybrid CNN + LSTM architecture      |
| DeepLSTM1_Indicadores1 | Deep LSTM with technical indicators |

**---**

**## 5. Solution Deployment**

**### Implemented Architecture**

```text
User
   ↓
Frontend FE_TSLA_V1_0 (Vercel)
   ↓
FastAPI REST API (Render)
   ↓
TensorFlow Runtime
   ↓
Selected Model
   ↓
TSLA Prediction
```

**### Frontend**

The frontend was deployed using Vercel and allows users to:

* Select a prediction date.

* Select the model to use.

* Query the prediction API.

* View the generated results.

**### Backend**

The backend was developed using FastAPI and deployed on Render.

Implemented endpoints:

| Endpoint       | Function                 |
| -------------- | ------------------------ |
| /health        | API status               |
| /models        | List of available models |
| /predict       | Prediction generation    |
| /latest-window | Retrieval of recent data |

**### Models Available in Production**

* LSTM

* LSTM1

* DeepLSTM1

* CNNLSTM1

The DeepLSTM1_Indicadores1 models were successfully trained but were not included in the final deployment due to additional dependencies associated with the calculation of technical indicators.

**---**

**## 6. Issues Encountered**

Several technical challenges were identified during deployment:

**### Dependency Compatibility**

The pandas_ta library used to generate technical indicators presented compatibility issues between the training environment and the production environment.

The version used during training could not be installed correctly on Render, preventing the a
