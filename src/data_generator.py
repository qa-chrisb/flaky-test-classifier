import pandas as pd
import random
import uuid
from datetime import datetime, timedelta

def generate_synthetic_data(num_tests=500):
	tests = []
	for _ in range(num_tests):
		test_id = str(uuid.uuid4())
		name = f"test_case_{random.randint(1, 100)}"
		execution_time = abs(random.gauss(5, 2))
		fail_rate = random.random()
		status = "fail" if fail_rate > 0.8 else "pass"
		retries = random.randint(0, 3) if status == "fail" else 0
		is_flaky = 1 if 0.75 < fail_rate < 0.85 else 0
		timestamp = datetime.now() - timedelta(days=random.randint(0, 30))
		tests.append([test_id, name, execution_time, status, retries, timestamp, is_flaky])

	df = pd.DataFrame(tests, columns=[
		"test_id", "name", "execution_time", "status", "retries", "timestamp", "is_flaky"
	])
	df.to_csv("data/synthetic_test_data.csv", index=False)
	print("Synthetic test data generated.")