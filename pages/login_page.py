from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from config.config import Config
import allure

class LoginPage(BasePage):
    
    def load(self):
        self.open_url(Config.BASE_URL)

    @allure.step("Performing Login")
    def login(self, username, password):
        self.type_text(LoginLocators.USERNAME_INPUT, username)
        self.type_text(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(LoginLocators.ERROR_MESSAGE)