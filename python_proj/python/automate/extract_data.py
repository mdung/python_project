import requests
import csv
from datetime import datetime
import os

def extract_live_post_data(api_url):
    # Make an HTTP request to the API endpoint
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON content
        posts = response.json()

        # Extract post data and prepare data for CSV
        data_for_csv = [(post.get('id'), post.get('title'), post.get('body')) for post in posts]

        # Create the 'output' folder if it doesn't exist
        output_folder = 'output'
        os.makedirs(output_folder, exist_ok=True)

        # Generate a meaningful name for the CSV file
        current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        csv_file_name = os.path.join(output_folder, f"live_post_data_{current_date}.csv")

        # Write data to CSV file
        with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Write header
            csv_writer.writerow(['ID', 'Title', 'Body'])

            # Write data rows
            csv_writer.writerows(data_for_csv)

        print(f"Data saved to {csv_file_name}")

    else:
        print(f"Failed to fetch the API. Status Code: {response.status_code}")

# Example usage:
api_url_to_scrape_live_posts = "https://jsonplaceholder.typicode.com/posts"
extract_live_post_data(api_url_to_scrape_live_posts)
