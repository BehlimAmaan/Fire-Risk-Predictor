import numpy as np
import pickle
from flask import Flask, render_template, request

application = Flask(__name__)
app = application

# Load model and scaler
ridge_model = pickle.load(open('Models/ridgereg.pkl', 'rb'))
standard_scaler = pickle.load(open('Models/scalar.pkl', 'rb'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET"])
def predict_page():
    return render_template("predict.html")

@app.route("/result", methods=["POST"])
def result():
    Temperature = float(request.form.get("Temperature"))
    RH = float(request.form.get("RH"))
    Ws = float(request.form.get("Ws"))
    Rain = float(request.form.get("Rain"))
    FFMC = float(request.form.get("FFMC"))
    DMC = float(request.form.get("DMC"))
    DC = float(request.form.get("DC"))   
    ISI = float(request.form.get("ISI"))
    Classes = float(request.form.get("Classes"))
    Region = float(request.form.get("Region"))

    input_data = [[Temperature, RH, Ws, Rain, FFMC, DMC, DC, ISI,Classes, Region]]
    scaled_data = standard_scaler.transform(input_data)

    prediction = ridge_model.predict(scaled_data)

    # THIS renders the result page
    return render_template("result.html", prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)
