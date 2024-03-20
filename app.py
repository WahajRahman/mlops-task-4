# app.py

from flask import Flask, request, jsonify
from predict_salary import predict

# Flask app instance
app = Flask(__name__)

# Define endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict_salary():
    # Get data from request
    data = request.json
    
    # Perform prediction
    prediction = predict(data)
    
    # Return prediction as JSON response
    return jsonify({'prediction': prediction})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
