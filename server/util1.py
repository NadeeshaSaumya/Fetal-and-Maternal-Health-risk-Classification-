# maternal health
import pickle
import json
import numpy as np

__data_columns = None
__model = None
__scaler = None


def get_predicted_materal_health_state(Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate):
    x = np.zeros(len(__data_columns))
    x[0] = Age
    x[1] = SystolicBP
    x[2] = DiastolicBP
    x[3] = BS
    x[4] = BodyTemp
    x[5] = HeartRate
    x_scaled = __scaler.transform([x])
    return __model.predict(x_scaled)[0]


def load_saved_artifacts():
    print("loading saved artifacts...start")

    global __data_columns
    with open("./artifacts/mat_columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
    print("loading saved artifacts...done")

    global __model
    if __model is None:
        with open('./artifacts/mat_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved model...done")

    global __scaler
    if __scaler is None:
        with open('./artifacts/mat_scaler.pickle', 'rb') as f:
            __scaler = pickle.load(f)
    print("loading saved scaler...done")


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_predicted_materal_health_state(0.250000, 0.666667, 0.607843, 0.692308, 0.0, 0.951807))
    print(get_predicted_materal_health_state(35, 120, 60, 6.1, 98.0, 76))
