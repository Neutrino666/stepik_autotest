from math import sin, log
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/execute_script.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, "input_value").text)
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.ID, "answer").send_keys(log(abs(12*sin(x))))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CLASS_NAME, 'btn').click()

    #  Выведет в консоль номер решения
    print(browser._switch_to.alert.text)

finally:
    sleep(5)
    browser.quit()
