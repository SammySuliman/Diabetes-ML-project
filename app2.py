import numpy as np
from flask import Flask, request,render_template
import pickle
from transitioner2 import Transitioner2

app = Flask(__name__)
diabetes_model = pickle.load(open('diabetes_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    prediction = diabetes_model.predict([Transitioner2(features)])

    output = prediction[0]

    if float(output) == 0.0:
        return render_template('index3.html', prediction_text='You are not at risk for developing diabetes'.format(output))
    elif float(output) == 1.0:
        return render_template('index3.html', prediction_text='You are at risk for developing diabetes-- please talk to your personal healthcare provider'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
