import requests
import csv
from datetime import datetime
import os

def extract_data_from_api(api_url):
    # Make an HTTP request to the API endpoint
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON content
        data = response.json()

        # Extract data fields dynamically
        if data:
            fields = list(data[0].keys())
            data_for_csv = [tuple(post[field] for field in fields) for post in data]

            # Create the 'output' folder if it doesn't exist
            output_folder = 'output'
            os.makedirs(output_folder, exist_ok=True)

            # Generate a meaningful name for the CSV file
            current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            csv_file_name = os.path.join(output_folder, f"data_{current_date}.csv")

            # Write data to CSV file
            with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)

                # Write header
                csv_writer.writerow(fields)

                # Write data rows
                csv_writer.writerows(data_for_csv)

            print(f"Data saved to {csv_file_name}")

        else:
            print("No data to extract.")

    else:
        print(f"Failed to fetch the API. Status Code: {response.status_code}")

# Example usage:
api_url_to_scrape = input("Enter the API URL to scrape: ")
extract_data_from_api(api_url_to_scrape)
