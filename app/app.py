import csv
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import joblib
import pickle
from pickle import load
import numpy as np

app = Flask(__name__)

# Load the trained classification model
with open('./static/data/trained_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET','POST'])
def index(prediction=None):
    return render_template('index.html', prediction=prediction)

@app.route('/send', methods=["POST"])
def send():
    # Retrieve the Zip code from the form
    zip_code = request.form['Zip']

    # Preprocess the input (convert to numeric feature)
    processed_zip_code = float(zip_code)

    # Print the processed Zip code to the terminal (for debugging purposes)
    print(processed_zip_code)

    # Perform prediction using the loaded model
    prediction = model.predict(np.array([processed_zip_code]).reshape(1, -1))[0]
    
    # Decide the result message based on the prediction
    if prediction == 0:
        result = "Restaurants In This Neighborhood are Typically Safe"
    else:
        result = "Restaurants In This Neighborhood are Typically Risky"

    # Render the result in the 'index.html' template
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)