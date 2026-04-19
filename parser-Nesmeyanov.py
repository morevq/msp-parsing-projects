import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

def parse_quotes():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', class_='quote')
    
    print(f"--- Quotes from {url} ---\n")
    for item in items:
        text = item.find('span', class_='text').text
        author = item.find('small', class_='author').text
        tags = [tag.text for tag in item.find_all('a', class_='tag')]
        
        print(f"Quote: {text}")
        print(f"Author: {author}")
        print(f"Tags: {', '.join(tags)}")
        print("-" * 40)

if __name__ == "__main__":
    parse_quotes()
