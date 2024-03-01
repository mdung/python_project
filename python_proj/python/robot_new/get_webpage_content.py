import requests
from bs4 import BeautifulSoup

def get_webpage_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return None

def parse_webpage_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Extracting information from different HTML elements
    title = soup.title.text.strip() if soup.title else "No Title Found"
    meta_description = soup.find("meta", {"name": "description"})
    description = meta_description["content"].strip() if meta_description else "No Description Found"

    # Extract text from all paragraphs
    paragraphs = soup.find_all('p')
    content = '\n'.join([p.get_text() for p in paragraphs])

    # Extracting all links
    links = [a['href'] for a in soup.find_all('a', href=True)]

    # Create a dictionary with extracted information
    webpage_info = {
        "Title": title,
        "Description": description,
        "Content": content,
        "Links": links,
    }

    return webpage_info

def save_to_txt(info_dict, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for key, value in info_dict.items():
            file.write(f"{key}:\n{value}\n\n")

def main():
    # Input: Get the URL from the user
    url = input("Enter the website link: ")

    # Fetch webpage content
    html_content = get_webpage_content(url)

    if html_content:
        # Parse webpage content
        webpage_info = parse_webpage_content(html_content)

        # Create a text file with a meaningful name
        output_filename = f"{url.replace('http://', '').replace('https://', '').replace('.', '_').replace('/', '_')}_info.txt"
        save_to_txt(webpage_info, output_filename)

        print(f"Webpage information saved to {output_filename}")
    else:
        print("Failed to fetch webpage content.")

if __name__ == "__main__":
    main()
