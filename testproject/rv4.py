# 5. Feladat: Kakukktojás - városok - Feladatod, hogy megtaláld a hiányzó városnevet, kitöltsd a form-ban a mezőt és ellnörizd le, hogy eltaláltad-e.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/rv4.html")
    time.sleep(2)

    # Make a list from the cities:
    cities = driver.find_element_by_id("cities").get_attribute("value")

    # Make an other list from the ramdom cities:
    random_cities = driver.find_elements_by_xpath('//*[@id="randomCities"]/li')
    random_city_list = []

    for city in random_cities:
        random_city_list.append(city.get_attribute("value"))

    # Check if the cities are amoung random_city_list elements, if it finds the missing one, write it into missing_city input field:
    missing_city = driver.find_element_by_id("missingCity")
    for i in cities:
        if i in random_city_list:
            continue
        else:
            missing_city.send_keys(i)

    # Check the name is correct:
    result = driver.find_element_by_id("result")
    btn = driver.find_element_by_id("submit").click()
    time.sleep()

    assert result.get_attribute("value") == "Eltaláltad."

finally:
    pass
    # driver.close()
