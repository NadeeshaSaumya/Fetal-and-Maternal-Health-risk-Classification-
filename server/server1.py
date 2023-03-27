# maternal health
from flask import Flask, request, jsonify
import util1

app = Flask(__name__)


@app.route('/predict_maternal_health', methods=['POST'])
def predict_maternal_health():
    #print("POST predict_maternal_health")
    Age = float(request.form['Age'])
    print("age is", Age)
    SystolicBP = float(request.form['SystolicBP'])
    print("SystolicBP is", SystolicBP)
    DiastolicBP = float(request.form['DiastolicBP'])
    print("DiastolicBP is", DiastolicBP)
    BS = float(request.form['BS'])
    print("BS is", BS)
    BodyTemp = float(request.form['BodyTemp'])
    print("BodyTemp is", BodyTemp)
    HeartRate = float(request.form['HeartRate'])
    print("HeartRate is", HeartRate)

    response = jsonify({
        'estimated_maternal_state': util1.get_predicted_materal_health_state(Age, SystolicBP, DiastolicBP, BS, BodyTemp,
                                                                             HeartRate)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Maternal Health State Prediction...")
    util1.load_saved_artifacts()
    app.run()
