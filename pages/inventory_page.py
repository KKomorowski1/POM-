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
    
    @allure.step("Get list of all products on inventory page")
    def get_all_products(self):
        return self.find_elements(InventoryLocators.LIST_OF_PRODUCTS)
    
    @allure.step("Get title of all products")
    def get_title_for_all_products(self):
        elements = self.find_elements(InventoryLocators.LIST_OF_PRODUCTS)
        return [element.text for element in elements]
        
    @allure.step("Sorting inventory by: {value}")
    def sort_by(self, value):
        self.select_by_value(InventoryLocators.SORT_DROPDOWN, value)