import tensorflow as tf

loadedModels = {}

def getModel(modelPath):

    modelPath = str(modelPath)

    if modelPath not in loadedModels:

        print(
            f"Loading model: {modelPath}"
        )

        loadedModels[modelPath] = (
            tf.keras.models.load_model(
                modelPath,
                compile=False
            )
        )

    return loadedModels[modelPath]