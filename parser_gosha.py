import requests
from bs4 import BeautifulSoup

page = requests.get("https://store.steampowered.com/search", verify=False)
soup = BeautifulSoup(page.text, "html.parser")

names = soup.find_all("span", class_="title")
prices = soup.find_all("div", class_="discount_final_price")
release_dates = soup.find_all("div", class_="search_released responsive_secondrow")

for i in range(len(names)):
    name = names[i].text
    price = prices[i].text
    release_date = release_dates[i].text.strip()
    print(name.ljust(35), price.rjust(15), release_date.rjust(20))