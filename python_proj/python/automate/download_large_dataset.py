import os
import requests
import pandas as pd

def download_large_dataset(url, download_path):
    # Create the download directory if it doesn't exist
    os.makedirs(download_path, exist_ok=True)

    # Extract the filename from the URL
    file_name = os.path.join(download_path, url.split("/")[-1])

    # Download the dataset
    print(f"Downloading dataset from {url}")
    response = requests.get(url, stream=True)
    with open(file_name, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

    print(f"Download complete. Dataset saved to {file_name}")
    return file_name

def process_large_csv(file_path):
    # Read the CSV file using pandas or any other suitable library
    df = pd.read_csv(file_path)

    # Perform data processing tasks
    # For example, print the first few rows of the dataframe
    print("First few rows of the dataset:")
    print(df.head())

def main():
    # Specify the URL of the large dataset
    dataset_url = 'https://www.kaggle.com/datasets/louise2001/quantum-physics-articles-on-arxiv-1994-to-2009'

    # Specify the local directory to save the downloaded dataset
    download_directory = 'download'

    # Download the dataset
    dataset_file = download_large_dataset(dataset_url, download_directory)

    # Process the downloaded dataset
    process_large_csv(dataset_file)

if __name__ == "__main__":
    main()
