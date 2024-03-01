import requests
from bs4 import BeautifulSoup

# Sample data input (replace this with the URL of the website you want to scrape)
url = 'http://vnexpress.net/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract specific data (replace this with the actual HTML structure of the website)
# In this example, we'll extract all the text within paragraph tags <p>
paragraphs = soup.find_all('p')

# Print the extracted data
for paragraph in paragraphs:
    print(paragraph.get_text())
