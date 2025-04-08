# Flaky Test Classifier

A simple machine learning pipeline that detects flaky tests based on historical test data.

## Usage

### 1. Activate environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Generate data:

```bash
python -m src.data_generator
```

### 3. Train the model:

```bash
python -m src.train_model
```

### 4. Predict flaky tests:

```bash
python cli.py --input data/synthetic_test_data.csv
```

---
