from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys("test@test.com")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    sleep(5)
    browser.quit()