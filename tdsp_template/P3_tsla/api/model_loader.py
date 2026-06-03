import tensorflow as tf

from P3_tsla.api.constants import (
    MODEL_PATH
)

model = tf.keras.models.load_model(
    MODEL_PATH,
    compile=False
)