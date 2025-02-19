"""
This script performs inference using a trained AutoGluon model.
It loads preprocessed test data, makes predictions, and saves the results.
"""

import os

from autogluon.tabular import TabularDataset, TabularPredictor

# Get the absolute path of the project's root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_inference():
    """
    Loads a trained model, runs predictions on test data, and saves the results.

    Steps:
    1. Load the preprocessed test dataset.
    2. Load the trained AutoGluon model.
    3. Generate predictions.
    4. Save predictions to a CSV file.
    """

    # Define file paths dynamically
    test_path = os.path.join(BASE_DIR, "data", "inference", "test_preprocessed.csv")
    output_path = os.path.join(BASE_DIR, "data", "predictions", "predictions.csv")

    # Load the preprocessed test dataset
    test_data = TabularDataset(test_path)

    # Load the trained AutoGluon model from the 'models' directory
    predictor = TabularPredictor.load(os.path.join(BASE_DIR, "models"))

    # Generate predictions
    predictions = predictor.predict(test_data)

    # Ensure the output directory exists before saving predictions
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save predictions to a CSV file
    predictions.to_csv(output_path)

    print("Predictions saved!")
