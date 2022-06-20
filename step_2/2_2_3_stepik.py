from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    Select(browser.find_element(By.ID, "dropdown"))\
        .select_by_value(str(num2 + num1))
    browser.find_element(By.CLASS_NAME, 'btn').click()
    #  Выведет в консоль номер решения
    print(browser._switch_to.alert.text)

finally:
    sleep(5)
    browser.quit()