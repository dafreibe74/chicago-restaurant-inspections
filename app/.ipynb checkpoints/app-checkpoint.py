
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load your trained model
model = joblib.load('../data/trained_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the zip code from the request
    zip_code = request.json['zip']
    
    # Use your model to make a prediction
    prediction = model.predict([[zip_code]])
    
    # Send a response based on the prediction
    if prediction[0] == 1:
        return jsonify({'risk': 'Restaurants Here are Typically Risky'})
    else:
        return jsonify({'risk': 'Restaurants Here are Typically Safe'})

if __name__ == '__main__':
    app.run(debug=True)


