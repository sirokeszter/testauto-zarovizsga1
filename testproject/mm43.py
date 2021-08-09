# 4. Feladat: Email mező

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/mm43.html")
    time.sleep(2)


    def check_email(mail):
        input_mail = driver.find_element_by_id("email")
        btn = driver.find_element_by_id("submit")

        input_mail.clear()
        input_mail.send_keys(mail)
        btn.click()
        time.sleep(3)


    error_msg = driver.find_element_by_xpath('//div[@class="validation-error"]')

    # TC01: Helyes kitöltés esete: email: teszt@elek.hu, Nincs validációs hibazüzenet
    check_email("teszt@elek.hu")
    assert not error_msg.get_attribute("value").is_displayed()

    # TC02: Helytelen: * email: teszt@, Please enter a part following '@'. 'teszt@' is incomplete.
    check_email("teszt@")
    assert error_msg.get_attribute("value") == "Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes."

    # TC03: Üres: email: <üres>, Please fill out this field.
    check_email("")
    assert error_msg.get_attribute("value") == "Kérjük, töltse ki ezt a mezőt."

finally:
    pass
    # driver.close()
