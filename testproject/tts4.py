# 2 Feladat: Pénzfeldobás - Az alkalmazás akkor működik helyesen ha 100 gombnyomásból legalább 30 fej. Ezt kell ellenőrizned.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/tts4.html")
    time.sleep(2)

    # Select the locators:
    btn = driver.find_element_by_id("submit")
    result = driver.find_element_by_id("lastResult")

    # Select the first 100 tosses in a list:
    toss_res = 0
    for toss in range(101):
        btn.click()
        if result.text == "fej":
            toss_res += 1

    # Checking the number of the "fej" if it's >= 30:
    assert toss_res >= 30

finally:
    pass
    # driver.close()