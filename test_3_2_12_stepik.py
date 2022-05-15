import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestAbs(unittest.TestCase):

    expected_text = "Congratulations! You have successfully registered!"
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"

    def engine_case(self, url):

        browser = webdriver.Chrome()
        browser.get(url)

        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys("test@test.com")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        sleep(1)
        self.welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    def test_abs1(self):
        self.engine_case(self.link1)
        self.assertEqual(
            self.expected_text, self.welcome_text,
            f"expected {self.expected_text}, got {self.welcome_text}"
        )

    def test_abs2(self):
        self.engine_case("http://suninjuly.github.io/registration2.html")
        self.assertEqual(
            self.expected_text, self.welcome_text,
            f"expected {self.expected_text}, got {self.welcome_text}"
        )


if __name__ == "__main__":
    unittest.main()
