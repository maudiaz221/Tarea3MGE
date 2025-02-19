from prep import prep_data
from train import train_model
from inference import run_inference

def main():
    # Preprocess raw data
    prep_data()

    # Train a model
    train_model()

    # Make predictions
    run_inference()


if __name__ == '__main__':
    main()
