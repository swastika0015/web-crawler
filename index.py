import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(urls, max_pages=4):
    visited = set()
    to_visit = set(urls)
    
    while to_visit and len(visited) < max_pages:
        url = to_visit.pop()
        
        try:
            response = requests.get(url)
            visited.add(url)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Print the title of the page
            title = soup.find('title')
            print(f"URL: {url}")
            print(f"Title: {title.string if title else 'No title'}\n")
            
            # Find all links on the page
            for link in soup.find_all('a'):
                href = link.get('href')
                if href:
                    full_url = urljoin(url, href)
                    if full_url not in visited:
                        to_visit.add(full_url)
        
        except Exception as e:
            print(f"Error crawling {url}: {e}\n")

# Example usage
start_urls = [
    "https://x.com/swastika0015",
    "https://www.linkedin.com/in/swastika15"
]

crawl(start_urls)