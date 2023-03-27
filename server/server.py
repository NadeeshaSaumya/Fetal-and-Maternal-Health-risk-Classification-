from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/predict_fetal_health', methods=['POST'])
def predict_fetal_health():
    ASTV = float(request.form['ASTV'])
    ALTV = float(request.form['ALTV'])
    AC = float(request.form['AC'])
    Median = float(request.form['Median'])
    Mean = float(request.form['Mean'])
    MSTV = float(request.form['MSTV'])
    DP = float(request.form['DP'])
    Mode = float(request.form['Mode'])
    Max = float(request.form['Max'])
    LB = float(request.form['LB'])
    MLTV = float(request.form['MLTV'])
    UC = float(request.form['UC'])

    response = jsonify({
        'estimated_fetal_state': util.get_predicted_fetal_health_state(ASTV, ALTV, AC, Median, Mean, MSTV, DP, Mode,Max, LB, MLTV, UC)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Fetal Health State Prediction...")
    util.load_saved_artifacts()
    app.run()
