from selenium.webdriver.common.by import By

class InventoryLocators:
    TITLE = (By.XPATH, "//span[@class='title']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    LIST_OF_PRODUCTS = (By.XPATH, "//div[@data-test='inventory-item']")
    LIST_OF_PRODUCTS_TITLES = (By.XPATH, "//div[@data-test='inventory-item-name']")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    @staticmethod
    def get_add_to_cart_btn(product_name):
        """
        Returns the locator tuple for a specific product's add button.
        Logic: Converts 'Sauce Labs Backpack' -> 'sauce-labs-backpack'
        """
        slug = product_name.lower().replace(" ", "-")
        return (By.ID, f"add-to-cart-{slug}")