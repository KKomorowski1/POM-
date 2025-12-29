from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = Config.TIMEOUT

    def open_url(self, url):
        with allure.step(f"Navigating to {url}"):
            self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        with allure.step(f"Clicking element: {locator}"):
            self.find_element(locator).click()

    def type_text(self, locator, text):
        with allure.step(f"Typing '{text}' into {locator}"):
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text