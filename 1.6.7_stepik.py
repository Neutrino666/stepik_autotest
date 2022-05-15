from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, "input")

    for element in elements:
        element.send_keys("Мой ответ")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    print(browser._switch_to.alert.text)

finally:
    sleep(10)
    browser.quit()