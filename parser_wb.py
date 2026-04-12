# ЕСЛИ ЧТО НУЖНО СОЗДАТЬ ПАПКУ selenium_profile РЯДОМ С ФАЙЛОМ


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json, time, os

url = "https://www.wildberries.ru/catalog/0/search.aspx?search=телефон"

options = Options()

base_dir = os.path.dirname(os.path.abspath(__file__))

profile_path = os.path.join(base_dir, "selenium_profile")

options.add_argument(f"--user-data-dir={profile_path}")

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

driver.get(url)

wait = WebDriverWait(driver, 30)

wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "product-card"))
)



cards_count = 0
scroll_pause = 0.5
scroll_step = 400
same_count_times = 0

while True:
    driver.execute_script(f"window.scrollBy(0, {scroll_step});")
    time.sleep(scroll_pause)

    cards_new = driver.find_elements(By.CLASS_NAME, "product-card")

    if len(cards_new) == cards_count:
        same_count_times += 1
    else:
        same_count_times = 0

    if same_count_times >= 5:
        break

    cards_count = len(cards_new)



cards = driver.find_elements(By.CLASS_NAME, "product-card")

dictionary: dict = {}

for card in cards:
    try:
        link_el = card.find_element(By.CLASS_NAME, "product-card__link")
        title = link_el.get_attribute("aria-label")
        link = link_el.get_attribute("href")
        
        try:
            brand_wrap = card.find_element(By.CLASS_NAME, "product-card__brand-wrap")
            brand_el = brand_wrap.find_element(By.CLASS_NAME, "product-card__brand")
            brand = brand_el.text.strip()
            if not brand:
                brand = "Не указан"
        except:
            brand = "Не указан"
        
        try:
            rating_wrap = card.find_element(By.CLASS_NAME, "product-card__rating-wrap")
            rating = rating_wrap.find_element(By.CLASS_NAME, "address-rate-mini").text
            count_feedback = rating_wrap.find_element(By.CLASS_NAME, "product-card__count").text
            if not rating:
                rating = "Отсутствует"
            if not count_feedback:
                count_feedback = "Отсутствуют"
        except:
            rating = "Отсутствует"
            count_feedback = "Отсутствуют"
        
        dictionary.update({
            title : {
                "link" : link,
                "brand" : brand,
                "rating" : rating,
                "count_feedback" : count_feedback
            }
        }
        )
    except:
        continue
    
print(json.dumps(dictionary, indent=4, ensure_ascii=False))

driver.quit()


# ЕСЛИ ЧТО НУЖНО СОЗДАТЬ ПАПКУ selenium_profile РЯДОМ С ФАЙЛОМ