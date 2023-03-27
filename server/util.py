import pickle
import json
import numpy as np
import pandas as pd
import xgboost

__data_columns = None
__model = None
__scaler = None


def get_predicted_fetal_health_state(ASTV, ALTV, AC, Median, Mean, MSTV, DP, Mode, Max, LB, MLTV, UC):
    column_names = ['ASTV', 'ALTV', 'AC', 'Median', 'Mean', 'MSTV', 'DP', 'Mode', 'Max', 'LB', 'MLTV', 'UC']
    x = np.zeros(len(__data_columns))
    x[0] = ASTV
    x[1] = ALTV
    x[2] = AC
    x[3] = Median
    x[4] = Mean
    x[5] = MSTV
    x[6] = DP
    x[7] = Mode
    x[8] = Max
    x[9] = LB
    x[10] = MLTV
    x[11] = UC

    x_scaled = __scaler.transform([x])
    data = pd.DataFrame(x_scaled, columns=column_names)
    #print(data)


    if (__model.predict(data)[0]==0):
        HS = "Normal"
    elif (__model.predict(data)[0]==1):
        HS = "Suspect"
    else:
        HS = "Pathalogic"
    return HS



def load_saved_artifacts():
    print("loading saved artifacts...start")

    global __data_columns
    with open("./artifacts/fet_columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
    print("loading saved artifacts...done")

    global __model
    if __model is None:
        with open('./artifacts/fet_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved model...done")

    global __scaler
    if __scaler is None:
        with open('./artifacts/fetal_scaler.pickle', 'rb') as f:
            __scaler = pickle.load(f)
    print("loading saved scaler...done")


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_predicted_fetal_health_state(73, 43, 0, 121, 137, 0.5, 0, 120, 126, 120, 2.4, 0))

