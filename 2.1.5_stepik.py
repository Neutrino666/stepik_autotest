from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"

    browser = webdriver.Chrome()
    browser.get(link)

    answer = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()
    browser.find_element(By.CSS_SELECTOR, '.container button').click()

    print(browser._switch_to.alert.text)

finally:
    sleep(5)
    browser.quit()