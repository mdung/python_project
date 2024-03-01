# Cloud Recommendation System

This project implements a cloud resource recommendation system using AI and DevOps practices.

## Project Structure

- **data/**: Contains the dataset used for training and testing the model (`usage_data.csv`).

- **models/**: Holds scripts related to model training (`train_model.py`) and the trained model file (`decision_tree_model.pkl`).

- **api/**: Contains the API-related files, such as the Flask app script (`app.py`).

- **scripts/**: Includes scripts for data preprocessing (`preprocess_data.py`).

- **requirements.txt**: Lists the Python packages required for your project.

- **README.md**: Documentation for your project, explaining its purpose, how to set it up, and any other relevant information.

- **main.py**: A script to demonstrate how to use the recommendation system. This script might include example code for sending new data to the API and receiving recommendations.

## Getting Started

1. Install dependencies: `pip install -r requirements.txt`
2. Train the model: `python models/train_model.py`
3. Run the API: `python api/app.py`
