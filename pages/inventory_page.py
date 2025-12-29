from pages.base_page import BasePage
from locators.inventory_locators import InventoryLocators
import allure

class InventoryPage(BasePage):
    
    @allure.step("Adding product to cart: {product_name}")
    def add_to_cart(self, product_name):
        # Get the specific tuple from the Locators class
        locator = InventoryLocators.get_add_to_cart_btn(product_name)
        self.click(locator)

    @allure.step("Getting cart item count")
    def get_cart_count(self):
        return self.get_text(InventoryLocators.CART_BADGE)