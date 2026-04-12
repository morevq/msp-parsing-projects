import requests
from bs4 import BeautifulSoup

url = 'https://www.aviasales.ru/search/MOW2803UFA05041'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("div")
print(len(title))
paragraphs = soup.find_all('p')

print(title)
for p in paragraphs:
    print(p.text.text)