import numpy as np
from tensorflow.keras.layers import TFSMLayer
import joblib

model = TFSMLayer("api/models/revenue/", call_endpoint="serving_default")
scaler = joblib.load("api/models/scaler/revenue_scaler.pkl")

DAYS=7
WINDOW_SIZE=3

def predict(revenues):
    revenues = np.array(revenues).reshape(-1, 1)
    scaled_revenues = scaler.fit_transform(revenues)
    
    result = []

    for _ in range(DAYS):
        input = scaled_revenues.reshape(1, WINDOW_SIZE, 1)

        scaled_prediction = model(input)
        scaled_prediction = list(scaled_prediction.values())[0]
        
        prediction = scaler.inverse_transform(scaled_prediction)
        prediction = int(np.round(prediction[0][0], -3))
        result.append(prediction)

        revenues = np.append(revenues, prediction)
        revenues = revenues[1:]
        revenues = np.array(revenues).reshape(-1, 1)

        scaled_revenues = scaler.transform(revenues)

    return result