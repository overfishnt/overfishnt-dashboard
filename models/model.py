from keras.models import load_model
from numpy import array
import os


# HEATMAP PARTS
# Get path to model heatmap
def get_heatmap_model(x:str):
    path = os.path.dirname(
        os.path.abspath(__file__)
    ) + "/models/heatmaps/Heatmap_{0}.h5".format(x)
    return load_model(path)

# Get path to model swh
def get_swh_model(x:str):
    path = os.path.dirname(
        os.path.abspath(__file__)
    ) + "/models/swh/modelswh{0}.h5".format(x.lower())
    return load_model(path)

# Get path to model presipitasi
def get_presipitasi_model(x:str):
    path = os.path.dirname(
        os.path.abspath(__file__)
    ) + "/models/presipitasi/csvpresipitasi{0}.h5".format(x.lower())
    return load_model(path)

# Get path to model angin
def get_angin_model(x:str):
    path = os.path.dirname(
        os.path.abspath(__file__)
    ) + "/models/angin/modelmodelangin{0}.h5".format(x.lower())
    return load_model(path)

# Predict heatmap with model
def predict_model(x, model):
    data = array(x).reshape((1, len(x), 1))
    prediction = model.predict(data)
    return list(prediction[0])