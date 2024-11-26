
# Flower Prediction ML Model API

This is a Flask-based API that predicts the type of flower based on its features (e.g., sepal length, sepal width, petal length, petal width). The model is trained on a dataset like the Iris dataset and uses a Machine Learning model for predictions.

---

## Features

- RESTful API for flower type prediction.
- Input validation for feature values.
- Lightweight and easy to deploy.
- Pre-trained Machine Learning model integrated.

---

## Prerequisites

- Python 3.8+
- Flask

---

## Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/m07amed25/Flower-Prediction---Deployment-Using-Flask
   cd Flower-Prediction---Deployment-Using-Flask
   ```

2. **Install Dependencies**  
   Use pip to install the required libraries:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Place the Model File**  
   Ensure your trained model (e.g., `model.pkl`) is in the root directory of the project.

---

## Usage

1. **Start the API**  
   Run the Flask application:
   ```bash
   python app.py
   ```
   By default, the app runs on `http://127.0.0.1:5000/`.

2. **Make Predictions**  
   Send a POST request to the `/predict` endpoint with the flower features in JSON format.

   **Example Request**:
   ```json
   POST /predict HTTP/1.1
   Content-Type: application/json

   {
       "sepal_length": 5.1,
       "sepal_width": 3.5,
       "petal_length": 1.4,
       "petal_width": 0.2
   }
   ```

   **Example Response**:
   ```json
   {
       "prediction": "Iris-setosa"
   }
   ```

---

## API Endpoints

### `POST /predict`

- **Description**: Predicts the type of flower based on input features.
- **Request Body**: JSON with the following fields:
  - `sepal_length` (float)
  - `sepal_width` (float)
  - `petal_length` (float)
  - `petal_width` (float)
- **Response**: 
  - `prediction` (str): Predicted flower type.

---

## File Structure

```
flower-prediction-api/
│
├── app.py               # Main Flask application
├── model.pkl            # Pre-trained ML model
└── README.md            # Documentation
```

---

## Example Code Snippets

### Python Client
```python
import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

response = requests.post(url, json=data)
print(response.json())
```

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author

**Mohamed Reda Ali**  
Machine Learning Specialist  
Feel free to connect with me for questions or collaboration!
