import csv
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import joblib
import pickle
from pickle import load
import numpy as np

app = Flask(__name__)

# # Ref: https://joblib.readthedocs.io/en/latest/auto_examples/compressors_comparison.html#sphx-glr-auto-examples-compressors-comparison-py
# # Load the trained classification model
# with open('./static/data/trained_model.pkl', 'rb') as file:
#     model = pickle.load(file)

@app.route('/', methods=['GET','POST'])
def index(prediction=None):

    return render_template('index.html', prediction=prediction)

@app.route('/send', methods=["POST"])
def send():
        
    prediction = 0

    zip_code = request.form['Zip']

    # Preprocess the input (convert to numeric feature)
    processed_zip_code = float(zip_code)

    # check terminal
    print(processed_zip_code)

#     # Perform prediction using the loaded model
#     prediction = model.predict(np.array([processed_zip_code]))[0]

    if prediction == 0:
        result = "Restaurants In This Neighborhood are Typically Safe"
    else:
        result = "Restaurants In This Neighborhood are Typically Risky"

    return render_template('index.html', prediction=result)


if __name__ == '__main__':
    app.run(debug=True)