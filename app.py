from flask import Flask, request, render_template

import pickle

import numpy as np

app = Flask(__name__)

import pickle
with open('modelbmi.pkl', 'rb') as fp:
    model = pickle.load(fp)

@app.route('/')
def index():
    return render_template('index.html', BMI=0)

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    prediction = model.predict(final_features)
    output = round(float(prediction[0], 2))
    return render_template('index.html', Weight=output)

if __name__ == '__name__':
    app.run(debug=True)