import pandas as pd

def preprocess_data(path):
	df = pd.read_csv(path)
	df["status"] = df["status"].map({"pass": 0, "fail": 1})
	df["timestamp"] = pd.to_datetime(df["timestamp"])
	df["days_since"] = (pd.Timestamp.now() - df["timestamp"]).dt.days
	features = df[["execution_time", "status", "retries", "days_since"]]
	labels = df["is_flaky"]
	return features, labels