import tensorflow as tf

from P3_tsla.api.constants import MODELS_DIR

modelPath = MODELS_DIR / "PT1_1_TSLA_5DAYS_LSTM.keras"

print("Model path:", modelPath)
print("File exists:", modelPath.exists())
print("TensorFlow:", tf.__version__)

model = tf.keras.models.load_model(modelPath, compile=False)

print("Model loaded successfully")