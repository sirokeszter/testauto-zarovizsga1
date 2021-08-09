# 3 Feladat: Összeadó (és egyéb műveletek)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html")
    time.sleep(2)

    # Select the locators:
    num1 = driver.find_element_by_id("num1").text
    print(num1)
    operator = driver.find_element_by_id("op").text
    num2 = driver.find_element_by_id("num2").text
    btn = driver.find_element_by_id("submit").click()
    time.sleep(2)

    # For calculation using eval inbuild function:
    if operator in ['+', '-', '*']:
        op_result = eval(num1 + operator + num2)

    print(int(op_result))

    result = driver.find_element_by_id("result")
    assert int(op_result) == int(result.text)


finally:
    pass
    # driver.close()
