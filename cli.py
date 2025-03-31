import argparse
from src.predict import classify_flaky_tests

def main():
	parser = argparse.ArgumentParser(description="Flaky Test Classifier")
	parser.add_argument("--input", type=str, help="Path to test result CSV")
	args = parser.parse_args()
	
	classify_flaky_tests(args.input)

if __name__ == "__main__":
	main()