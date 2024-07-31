import requests
from bs4 import BeautifulSoup
import re 
import urllib.parse

# Function to get Google search results
def get_google_search_results(query):
    # Format the query
    query = query.replace(' ', '+')
    url = f'https://www.google.com/search?q={query}'
    
    # Headers to mimic a browser visit
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    # Fetch the page
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f'Failed to retrieve search results. Status code: {response.status_code}')
        return None

# Function to extract links from Google search results
def extract_links_from_search_results(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all search result links
    links = []
    for item in soup.find_all('a'):
        href = item.get('href')
        if href and '/url?q=' in href:
            link = href.split('/url?q=')[1].split('&')[0]
            links.append(link)
    return links

"""
def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_pattern, text)

def scrape_emails(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')
        emails = extract_emails(soup.text)
        return set(emails)  
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return set()
websites = [
    'https://www.eonenglish.org/about-us',
    'https://oxylabs.io/blog/automated-web-scraper-autoscraper'

]
all_emails = set()
for site in websites:
    emails = scrape_emails(site)
    all_emails.update(emails)

print("Extracted Emails:")
for email in all_emails:
    print(email)
"""
# Main function to perform search and extract links
def main():
    keyword = 'Clean Energy'
    html_content = get_google_search_results(keyword)
    
    if html_content:
        links = extract_links_from_search_results(html_content)
        for link in links:
            print(link)

main()