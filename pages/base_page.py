from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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
    
    def find_elements(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
    
    def select_by_value(self, locator, value):
        """
        A universal tool to pick an option from ANY dropdown.
        """
        with allure.step(f"Selecting '{value}' from dropdown: {locator}"):
            element = self.find_element(locator)
            dropdown = Select(element)
            dropdown.select_by_value(value)