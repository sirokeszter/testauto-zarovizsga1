# 1. feladat

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/x234.html")
    time.sleep(2)


    def rectangle_perimeter(a, b):
        a_side = driver.find_element_by_id("a")
        b_side = driver.find_element_by_id("b")
        btn = driver.find_element_by_id("submit")

        a_side.clear()
        b_side.clear()

        a_side.send_keys(a)
        b_side.send_keys(b)
        btn.click()
        time.sleep(2)


    result = driver.find_element_by_id("result")

    # TC01: Helyes kitöltés esete: a: 99, b: 12, Eredmény: 222
    rectangle_perimeter(99, 12)
    assert result.text == "222"

    # TC02: Nem számokkal történő kitöltés: a: kiskutya, b: 12, Eredmény: NaN
    rectangle_perimeter("kiskutya", 12)
    assert result.text == "NaN"

    # TC03: Üres kitöltés: a: <üres>, b: <üres>, Eredmény: NaN
    rectangle_perimeter("", "")
    assert result.text == "NaN"

finally:
    pass
    # driver.close()
