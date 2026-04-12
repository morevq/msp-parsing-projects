import requests
from bs4 import BeautifulSoup

page = requests.get("https://cyberleninka.ru/article/")
soup = BeautifulSoup(page.text, "html.parser")
titles = soup.find_all("li")

for title in titles:
    print(title.text)