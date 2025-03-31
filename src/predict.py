import joblib
import pandas as pd
from src.preprocess import preprocess_data

def classify_flaky_tests(input_path):
	model = joblib.load("models/flaky_classifier.pkl")
	X, _ = preprocess_data(input_path)
	preds = model.predict(X)
	results = pd.read_csv(input_path)
	results["prediction"] = ["flaky" if p else "stable" for p in preds]
	print(results[["name", "prediction"]])