def main():
    # Добавьте свое имя и первую букву фамилии в этот список
    students = [
        "Иван И.",
        "Анна С.",
        "Петр В.",
        "Абгалдаев Е."
    ]
    
    print("Участники команды:")
    for student in students:
        print(f"- {student}")

if __name__ == "__main__":
    main()
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