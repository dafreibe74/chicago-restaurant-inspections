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
    # Preprocess the input (convert to numeric feature)
    zip_code = int(request.form['Zip'])
    result_encoded = int(request.form['result'])


    # Note:  'Fail' is one-hot-encoded as all zeros as well as 60601
    results_list = ['Fail','No Entry', 'Not Ready', 'Pass', 'Pass w/ Conditions']
    result_input = [0]*4
    if result_encoded != 4:
        result_input[result_encoded - 1] = 1

    zip_list = ['60601', '60602', '60603',
       '60604', '60605', '60606', '60607',
       '60608', '60609', '60610', '60611',
       '60612', '60613', '60614', '60615',
       '60616', '60617', '60618', '60619',
       '60620', '60621', '60622', '60623',
       '60624', '60625', '60626', '60628',
       '60629', '60630', '60631', '60632',
       '60633', '60634', '60636', '60637',
       '60638', '60639', '60640', '60641',
       '60642', '60643', '60644', '60645',
       '60646', '60647', '60649', '60651',
       '60652', '60653', '60654', '60655',
       '60656', '60657', '60659', '60660',
       '60661', '60666', '60707', '60827']
    zip_coded = [0]*58
    if zip_code !=58:
        zip_coded[zip_code-1] = 1  

    combined = result_input + zip_coded
    print(combined)


    # Perform prediction using the loaded model
    prediction = model.predict(np.array([combined]).reshape(1, -1))[0]
    print(prediction)
    # Decide the result message based on the prediction
    if prediction == 0:
        result = f"Restaurants In Zip Code {zip_list[zip_code]} with inspections results of {results_list[result_encoded]} are Typically Safe"
    else:
        result = f"Restaurants In Zip Code {zip_list[zip_code]} with inspections results of {results_list[result_encoded]}  are Typically Risky"

    # Render the result in the 'index.html' template
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)