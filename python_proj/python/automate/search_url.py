from googlesearch import search as google_search
import requests
from bs4 import BeautifulSoup
import os
import json

def search_finance_webpages(query, num_results=5):
    search_results = list(google_search(query, num_results=num_results))

    for i, url in enumerate(search_results, start=1):
        print(f"\nResult {i}: {url}")
        scrape_and_save_data(url, f"result_{i}")

def scrape_and_save_data(url, folder_name):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant information from the webpage
        title = soup.title.text.strip() if soup.title else 'N/A'
        description = soup.find('meta', {'name': 'description'})['content'].strip() if soup.find('meta', {'name': 'description'}) else 'N/A'
        article_content = soup.find('article').text.strip() if soup.find('article') else 'N/A'

        # Create a folder based on domain, date, and time
        domain_name = url.split("//")[-1].split("/")[0].replace(".", "_")
        folder_path = os.path.join('output_search', f"{domain_name}_{folder_name}")
        os.makedirs(folder_path, exist_ok=True)

        # Write data to JSON file
        json_file_name = os.path.join(folder_path, "webpage_data.json")
        data = {
            'URL': url,
            'Title': title,
            'Description': description,
            'ArticleContent': article_content,
        }

        with open(json_file_name, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)

        print(f"Data saved to {json_file_name}")

    else:
        print(f"Failed to fetch the URL. Status Code: {response.status_code}")

if __name__ == "__main__":
    search_query = input("Enter your search query for finance web pages: ")
    search_finance_webpages(search_query)
