from math import sin, log
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = " http://suninjuly.github.io/redirect_accept.html"

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, 'btn').click()
    browser.switch_to.window(browser.window_handles[1])
    x = int(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(log(abs(12 * sin(x))))
    browser.find_element(By.CLASS_NAME, 'btn').click()
    #  Выведет в консоль номер решения
    print(browser._switch_to.alert.text)

finally:
    sleep(5)
    browser.quit()
