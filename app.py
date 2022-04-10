from flask import Flask, request, render_template
import joblib
import numpy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', BMI=0)

@app.route('/predict', methods=['POST'])
def predict():
    Status_Gender, Height = [x for x in request.form.values()]
    
    data = []
    
    data.append(float(Status_Gender))
    data.append(float(Height))
    
    # Open trained model
    file = open("modelbmi.pkl","rb")
    
    # Load trained model
    trained_model = joblib.load(file)
    
    prediction = trained_model.predict([data])
    output = round(float(prediction[0], 2))
    return render_template('index.html', Weight=output, Status_Gender=Status_Gender, Height=Height)

if __name__ == '__name__':
    app.run(debug=True)