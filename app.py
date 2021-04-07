#!/usr/bin/python

import os, pickle, json
from flask import Flask, render_template, request,
from flask_bootstrap import Bootstrap
from utils import take_a_shower

# APP
app = Flask(__name__)
Bootstrap(app)

# Static path
static_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "static"))

# Some parameteres
MODEL_PATH = './model/svm_model_82.pkl'


# MODEL
def load_model():
    print('Loading model..')
    model = pickle.load(open(MODEL_PATH, 'rb'))
    print('Model Loaded.')
    return model


def classify(model, text):
    # Preprocessing
    text = take_a_shower(text)
    # Predict!
    result = model.predict([text])
    label = 'Offensive 🐶' if result[0] == 1 else 'Not-Offensive 🐱'
    return label

# LANDING
@app.route('/')
def index():
    return render_template('index.html')

# PROCESS
@app.route('/process', methods=['POST'])
def process():
    text = request.form['text']
    # Load model
    model = load_model()
    # Predict!
    label = classify(model, text)
    # Return Label 
    return json.dumps({'status':'OK','label':label})

if __name__ == '__main__':
    app.run(host='0.0.0.0')