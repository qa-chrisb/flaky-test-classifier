import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from src.preprocess import preprocess_data

def train_model():
	X, y = preprocess_data("data/synthetic_test_data.csv")
	clf = RandomForestClassifier(n_estimators=100, random_state=42)
	clf.fit(X, y)
	os.makedirs("models", exist_ok=True)
	joblib.dump(clf, "models/flaky_classifier.pkl")
	print("Model trained and saved.")

if __name__ == "__main__":
	train_model()
