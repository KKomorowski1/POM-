import pytest
import json
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# 1. Helper to load the User Roles dictionary
def get_users():
    with open('data/users.json') as f:
        return json.load(f)

# 2. Helper to load the Inventory Test Data (products)
def get_inventory_data():
    with open('data/inventory_data.json') as f:
        return json.load(f)

@allure.feature("Shopping Cart")
class TestInventory:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """
        Auto-login as a 'standard_user' before every test.
        """
        # Load the users file
        users = get_users()
        user_data = users['standard_user']  # Select the role you need

        # Perform Login using data from the file
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(user_data['username'], user_data['password'])

    @pytest.mark.parametrize("data", get_inventory_data())
    @allure.story("Add Single Product to Cart")
    def test_add_product(self, driver, data):
        inventory_page = InventoryPage(driver)
        
        inventory_page.add_to_cart(data['product_name'])
        
        assert inventory_page.get_cart_count() == data['cart_badge_expected']

    @allure.story("Check sorting")
    def test_sorting(self, driver):
        inventory_page =  InventoryPage(driver)
        inventory_page.get_all_products()
        default_sort = inventory_page.get_title_for_all_products()
        inventory_page.sort_by('za')
        sorted_za = inventory_page.get_title_for_all_products()

        assert sorted(default_sort, reverse = True) == sorted_za, f"Ordering A-Z failed"