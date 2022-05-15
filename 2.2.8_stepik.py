import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/file_input.html"

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Pupa")
    browser.find_element(By.NAME, "lastname").send_keys("Lupa")
    browser.find_element(By.NAME, "email").send_keys("test@test.com")
    browser.find_element(By.ID, 'file').send_keys(file_path)
    browser.find_element(By.CLASS_NAME, 'btn').click()

    #  Выведет в консоль номер решения
    print(browser._switch_to.alert.text)

finally:
    sleep(5)
    browser.quit()

# Пример для изучения
# import os
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/file_input.html')
#
# file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.txt')
#
# if not os.path.exists(file_path):
#     with open(file_path, 'w') as f:
#         pass
#
# inputs = ['Aleksey', 'Bychutkin', 'test@gmail.com', file_path]
#
# for element, value in zip(browser.find_elements_by_tag_name('input'), inputs):
#     element.send_keys(value)
#
# browser.find_element_by_css_selector('button.btn').click()