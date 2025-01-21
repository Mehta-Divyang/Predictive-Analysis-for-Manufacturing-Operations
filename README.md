# Manufacturing Prediction API

This project provides a RESTful API for predicting machine downtime or product defects in a manufacturing setup. Built with Flask and scikit-learn, it allows uploading datasets, training machine learning models, and making predictions.

---

## Features
- **Upload Data**: Upload a CSV file containing machine data.
- **Train Model**: Train a supervised ML model on the uploaded dataset.
- **Predict**: Make predictions based on input machine parameters.

---

## Setup Instructions

Follow these steps to set up and run the API:

### **Prerequisites**
- Python 3.7+
- Flask
- scikit-learn
- curl/Postman (for API testing)

### **Steps**
1. Clone this repository:
   ```bash
   git clone https://github.com/Mehta-Divyang/Predictive-Analysis-for-Manufacturing-Operations.git
   cd Predictive-Analysis-for-Manufacturing-Operations
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. The API will be available at:
   ```
   http://127.0.0.1:5000/
   ```

---

## Example API Requests and Responses

### **1. Upload Dataset**
Endpoint: `POST /upload`

- **Request**: Upload a CSV file (e.g., `machine_maintenance_data.csv`).
  ```bash
  curl -X POST -F "file=@machine_maintenance_data.csv" http://127.0.0.1:5000/upload
  ```
- **Response**:
  ```json
  {
    "columns": [
      "Machine_ID",
      "Temperature",
      "Run_Time",
      "Downtime_Flag"
    ],
    "message": "File uploaded Successfully!"
   }
  ```

---

### **2. Train Model**
Endpoint: `POST /train`

- **Request**: Start training the model.
  ```bash
  curl -X POST http://127.0.0.1:5000/train
  ```
- **Response**:
  ```json
  {
    "accuracy": 0.89,
    "message": "Model Trained Successfully!"
  }
  ```

---

### **3. Predict Downtime**
Endpoint: `POST /predict`

- **Request**: Send JSON data to make a prediction.
  ```bash
  curl -X POST -H "Content-Type: application/json" --data '{"Temperature": 309, "Run_Time": 48}'  http://127.0.0.1:5000/predict
  ```
- **Response**:
  ```json
  {    
    "Confidence": 0.72,
    "Downtime": "Yes"
  }
  ```

---

## Directory Structure
```
project_name/
│
├── app.py                  # Flask app
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── downtime_prediction.pkl # Serialized model
├── machine_maintenance_data.csv # Dataset file

```

---

## Contact
For questions or feedback, please open an issue in this repository.

