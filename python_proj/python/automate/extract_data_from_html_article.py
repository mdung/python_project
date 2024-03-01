import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os

def extract_data_from_html(api_url):
    # Make an HTTP request to the URL
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data from the HTML
        url = api_url
        title = soup.title.text.strip() if soup.title else 'N/A'
        description = soup.find('meta', {'name': 'description'})['content'].strip() if soup.find('meta', {'name': 'description'}) else 'N/A'

        # Extract photo (assuming the first image in the page)
        photos = soup.find_all('img')
        photo = photos[0]['src'].strip() if photos else 'N/A'

        # Extract article content (assuming the content is within the <article> tag)
        article_tag = soup.find('article')
        article_content = article_tag.text.strip() if article_tag else 'N/A'

        # Extract all links on the page
        links = []
        for link in soup.find_all('a', href=True):
            link_url = link['href'].strip()
            link_text = link.get_text().strip()
            links.append({'URL': link_url, 'Text': link_text})

        # Create a folder based on domain, date, and time
        domain_name = urlparse(api_url).netloc
        folder_name = f"{domain_name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
        folder_path = os.path.join('output', folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Write data to JSON file
        json_file_name = os.path.join(folder_path, "webpage_data.json")
        data = {
            'URL': url,
            'Title': title,
            'Description': description,
            'Photo': photo,
            'ArticleContent': article_content,
            'Links': links
        }

        with open(json_file_name, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)

        print(f"Data saved to {json_file_name}")

    else:
        print(f"Failed to fetch the URL. Status Code: {response.status_code}")

def process_multiple_urls():
    urls_to_scrape_html = input("Enter URLs to scrape (separated by commas): ").split(',')
    urls_to_scrape_html = [url.strip() for url in urls_to_scrape_html]

    for url in urls_to_scrape_html:
        extract_data_from_html(url)

# Example usage:
process_multiple_urls()
