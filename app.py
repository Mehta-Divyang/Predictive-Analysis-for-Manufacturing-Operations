from flask import Flask,request,jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,f1_score
import joblib

app = Flask(__name__)

model = None
data_file = None

@app.route('/')
def home():
    return "Welcome to the Manufacturing Prediction API."

@app.route('/upload', methods=['POST'])
def data_upload():
    global data_file
    '''if 'file' not in request.files:
        return jsonify({"error":"No file!"})'''
    file = request.files['file']

    if file.filename.endswith('.csv'):
        data_file = pd.read_csv(file)
        return jsonify({"message":"File uploaded Successfully!", "columns":list(data_file.columns)})
    
    else:
        return jsonify({"error":"Upload only .csv file"})
    
@app.route('/train', methods=['POST'])
def train_model():
    global data_file,model
    X = data_file[['Temperature','Run_Time']]
    y = data_file['Downtime_Flag']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    joblib.dump(model,'downtime_prediction.pkl')

    accuracy = accuracy_score(y_test, y_pred)

    return jsonify({"message":"Model Trained Successfully!","accuracy":accuracy})

@app.route('/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        try:
            model = joblib.load('downtime_prediction.pkl')
        except:
            return jsonify({"error":"No model found. Train a model first!"})
    
    try:
        input_data = request.get_json()
        temperature = input_data.get('Temperature')
        run_time = input_data.get('Run_Time')

        if run_time is None or temperature is None:
            return jsonify({"error":"Missing input data! Provide 'Temperature' and 'Run_Time' data"})

        prediction = model.predict([[temperature,run_time]])
        confidence = model.predict_proba([[temperature,run_time]]).max()

        return jsonify({"Downtime Flag":"Yes" if prediction == 1 else "No", "Confidence":confidence})
    
    except Exception as e:
        return jsonify({"error":str(e)})

if __name__ == "__main__":
    app.run(debug=False)

