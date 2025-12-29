import pytest
import json
import allure
from pages.login_page import LoginPage

# Load data from JSON
def get_data():
    with open('data/login_data.json') as f:
        return json.load(f)

@allure.feature("Login Feature")
class TestLogin:

    @pytest.mark.parametrize("data", get_data())
    @allure.story("Login Scenarios")
    def test_login_ddt(self, driver, data):
        login_page = LoginPage(driver)
        
        # 1. Open Page
        login_page.load()
        
        # 2. Perform Action
        login_page.login(data['username'], data['password'])
        
        # 3. Assert Result
        if data['scenario'] == "valid_login":
            assert "inventory" in driver.current_url
        elif data['scenario'] == "locked_user":
            assert data['expected_result'] in login_page.get_error_message()