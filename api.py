# fastapi_app.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
import pandas as pd
import joblib
from src.preprocess import preprocess_data
import os

app = FastAPI()

MODEL_PATH = "models/flaky_classifier.pkl"

@app.get("/", response_class=HTMLResponse)
def home():
	return """
	<html>
	<head><title>Flaky Test Classifier</title></head>
	<body>
	<h2>Upload a CSV file of test results</h2>
	<form action="/predict" enctype="multipart/form-data" method="post">
		<input name="file" type="file">
		<input type="submit">
	</form>
	</body>
	</html>
	"""

@app.post("/predict")
def predict_flakiness(file: UploadFile = File(...)):
	if not os.path.exists(MODEL_PATH):
		return {"error": "Model not trained. Please train the model first."}

	model = joblib.load(MODEL_PATH)
	uploaded_data = pd.read_csv(file.file)
	uploaded_data.to_csv("data/uploaded_temp.csv", index=False)
	X, _ = preprocess_data("data/uploaded_temp.csv")
	predictions = model.predict(X)
	uploaded_data["prediction"] = ["flaky" if p else "stable" for p in predictions]

	return uploaded_data[["name", "prediction"]].to_dict(orient="records")
