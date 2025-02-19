"""
This script trains a machine learning model using AutoGluon and saves it to a specified directory.

It dynamically constructs file paths to ensure portability across different environments.
"""

import os

from autogluon.tabular import TabularDataset, TabularPredictor


# Get the absolute path of the project's root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def train_model():
    """
    Loads preprocessed training data, trains a model using AutoGluon, and saves the model.

    Steps:
    1. Load preprocessed data from 'data/prep/train_preprocessed.csv'.
    2. Define a TabularPredictor using the 'SalePrice' target variable.
    3. Train the model using AutoGluon's `.fit()` method.
    4. Save the trained model in the 'models' directory.
    """

    # Define the target variable (what we want to predict)
    target = "SalePrice"

    # Construct the path to the preprocessed training data
    train_path = os.path.join(BASE_DIR, "data", "prep", "train_preprocessed.csv")

    # Load the preprocessed training dataset
    train_data = TabularDataset(train_path)

    # Define the path where the trained model will be saved
    save_path = os.path.join(BASE_DIR, "models")

    # Train the model using AutoGluon
    TabularPredictor(label=target, path=save_path).fit(train_data, time_limit=10)

    # Print the path
    print("Model training complete! Model saved at:", save_path)
