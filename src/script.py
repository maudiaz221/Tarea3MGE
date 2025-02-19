"""
This script runs the whole process of the pipeline
"""


from prep import prep_data
from train import train_model
from inference import run_inference

def main():
    """
    This function runs the 3 main parts of the pipeline
    - prep the data
    - train the model
    - run inference

    """
    # Preprocess raw data
    prep_data()

    # Train a model
    train_model()

    # Make predictions
    run_inference()


if __name__ == '__main__':
    main()
