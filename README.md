🩺 Diabetes Prediction Web App
This repository contains a **web-based application** for predicting whether a person is diabetic or not, based on their medical input data. The project uses a **Machine Learning (ML) model** built with scikit-learn
and a sleek flask frontend with a dark-themed interface.


📝 **Overview**

The Diabetes Prediction Web App allows users to input medical details such as glucose levels, BMI, age, and more. The app then uses a pre-trained ML model to predict if the person is **diabetic** or **not diabetic**.

✨ Features

- **Frontend**: A modern and visually appealing interface for user input.
- **Machine Learning Prediction**: Uses an SVM model trained on medical data.
- **Real-Time Results**: Immediate feedback on whether the person is diabetic or not.
- **Error Handling**: Ensures valid input and provides feedback for missing or incorrect entries.

---

## 🛠 **Technologies Used**

- **Frontend**: HTML5, CSS3 (dark theme design)
- **Backend**: Python Flask
- **Machine Learning**: Scikit-learn (SVM classifier)
- **Model Deployment**: Flask for serving the model

 📁 **Project Structure**

diabetes-prediction-app/
│
├── static/
│   └── style.css           # CSS for the dark theme (optional if inline styles are used)
│
├── templates/
│   └── index.html          # HTML for the frontend interface
│
├── models/
│   ├── svm_model.pkl       # Trained SVM model
│   └── scaler.pkl          # Scaler for preprocessing input data
│
└── app.py                  # Flask backend to handle predictions
└── README.md               # Project documentation
```

---

## ⚙️ **Setup Instructions**

### 1. **Clone the Repository**

```bash
git clone https://github.com/meghanacycarat/diabetes-predictor.git
cd diabetes
```

### 2. **Create and Activate a Virtual Environment**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS and Linux
source venv/bin/activate
```

### 3. **Install Dependencies**

```bash
pip install flask scikit-learn numpy pandas
```

### 4. **Ensure the Model Files Are in Place**

Make sure `svm_model.pkl` and `scaler.pkl` are present in the `models` directory. You can create these by training your model and saving it using `joblib` or `pickle`.

### 5. **Run the Flask App**

```bash
python app.py
```

### 6. **Access the Web App**

Go to `http://127.0.0.1:5000/` in your browser.

---

## 🚀 **Usage**

1. **Fill in the Form**: Enter the following medical details:
    - **Pregnancies**
    - **Glucose**
    - **Blood Pressure**
    - **Skin Thickness**
    - **Insulin**
    - **BMI**
    - **Diabetes Pedigree Function**
    - **Age**

2. **Submit the Form**: Click the **"Predict"** button.

3. **View Results**: The app will display whether the person is **Diabetic** or **Not Diabetic**.

---

## 🧪 **Sample Data**

You can use the following sample data for testing:

| Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI  | DiabetesPedigreeFunction | Age | Outcome  |
|-------------|---------|---------------|---------------|---------|------|--------------------------|-----|----------|
| 6           | 148     | 72            | 35            | 0       | 33.6 | 0.627                    | 50  | 1 (Diabetic) |
| 1           | 85      | 66            | 29            | 0       | 26.6 | 0.351                    | 31  | 0 (Not Diabetic) |

---

## 🌟 **Future Enhancements**

- **Add Graphical Visualizations** for the input data.
- **User Authentication** to save predictions for individual users.
- **Model Retraining** feature to allow users to retrain the model with new data.

---

## 🤝 **Contributing**

Contributions are welcome! If you'd like to improve this project, please:

1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Open a pull request.

---

### 🎉 **Thank You for Checking Out This Project!**

If you found this useful, please ⭐ star the repository!

---

Let me know if you'd like any modifications or additions! 🚀
