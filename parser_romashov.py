import requests
from bs4 import BeautifulSoup

page = requests.get("https://cyberleninka.ru/article/c/electrical-electronic-information-engineering")
soup = BeautifulSoup(page.text, "html.parser")
titles = soup.find_all("div", class_="title")

for title in titles:
    print(title.text)