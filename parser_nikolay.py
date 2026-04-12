import requests
from bs4 import BeautifulSoup

page = requests.get("https://kudamoscow.ru/event/all/week/")
# print(page.text)
soup = BeautifulSoup(page.text, "html.parser")
name = soup.find_all("h2")

for i in range(len(name)):
  print(name[i].text)