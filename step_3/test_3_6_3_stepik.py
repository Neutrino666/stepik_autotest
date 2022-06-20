import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

answer = math.log(int(time.time() + 36.2))
lesson_numbers = (
    "236895",
    "236896",
    "236897",
    "236898",
    "236899",
    "236903",
    "236904",
    "236905"
)


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    # time.sleep(10)
    browser.quit()


@pytest.mark.parametrize('number', [s for s in lesson_numbers])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "ember-text-area").send_keys(str(answer))
    # browser.find_element(By.ID, "submit-submission").click()
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "submit-submission"))
    )
    button.click()
    text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "ember-application").text)
    )

    assert "Correct!" in text, f"expected Correct! got {text}"

    # browser.find_element_by_css_selector("#ember90")
    # browser.find_element_by_css_selector(".submit-submission")