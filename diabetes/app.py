# app.py
from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load the saved model and scaler
classifier = joblib.load('svm_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form values
        input_data = [
            float(request.form['Pregnancies']),
            float(request.form['Glucose']),
            float(request.form['BloodPressure']),
            float(request.form['SkinThickness']),
            float(request.form['Insulin']),
            float(request.form['BMI']),
            float(request.form['DiabetesPedigreeFunction']),
            float(request.form['Age'])
        ]
        
        # Reshape and scale the data
        input_asnumpy = np.asarray(input_data).reshape(1, -1)
        std_data = scaler.transform(input_asnumpy)
        
        # Make prediction
        prediction = classifier.predict(std_data)
        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
        
        return render_template('index.html', prediction_text=f'The person is {result}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {e}')

if __name__ == '__main__':
    app.run(debug=True)
