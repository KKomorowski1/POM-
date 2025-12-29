# POM Selenium Project

This project implements a Selenium test automation framework using the Page Object Model (POM) design pattern for testing the SauceDemo website (https://www.saucedemo.com/).

## Project Structure

The project is organized into the following directories:

- `config/`: Configuration settings
- `data/`: Test data in JSON format
- `locators/`: Page element locators
- `pages/`: Page Object classes
- `tests/`: Test classes

## Classes Overview

### Config Class (`config/config.py`)
The `Config` class contains static configuration constants used throughout the project:
- `BASE_URL`: The base URL of the application under test ("https://www.saucedemo.com/")
- `TIMEOUT`: Default timeout for WebDriverWait operations (10 seconds)
- `BROWSER`: Default browser to use ("chrome")
- `HEADLESS`: Flag to run browser in headless mode (False by default)

### LoginLocators Class (`locators/login_locators.py`)
The `LoginLocators` class defines locator tuples for elements on the login page:
- `USERNAME_INPUT`: Locator for the username input field (By.ID, "user-name")
- `PASSWORD_INPUT`: Locator for the password input field (By.ID, "password")
- `LOGIN_BUTTON`: Locator for the login button (By.ID, "login-button")
- `ERROR_MESSAGE`: Locator for error message display (By.CSS_SELECTOR, "h3[data-test='error']")

### InventoryLocators Class (`locators/inventory_locators.py`)
The `InventoryLocators` class defines locator tuples for elements on the inventory/products page:
- `TITLE`: Locator for the page title (By.XPATH, "//span[@class='title']")
- `CART_BADGE`: Locator for the shopping cart badge showing item count (By.CLASS_NAME, "shopping_cart_badge")
- `get_add_to_cart_btn(product_name)`: Static method that dynamically generates the locator for a specific product's "Add to Cart" button based on the product name. It converts the product name to a slug format (e.g., "Sauce Labs Backpack" -> "sauce-labs-backpack") and returns (By.ID, f"add-to-cart-{slug}")

### BasePage Class (`pages/base_page.py`)
The `BasePage` class is the base class for all page object classes, providing common Selenium WebDriver operations:
- `__init__(driver)`: Initializes the page object with a WebDriver instance and sets the timeout from Config
- `open_url(url)`: Navigates to the specified URL with Allure reporting
- `find_element(locator)`: Waits for and returns a visible element located by the given locator
- `click(locator)`: Clicks on an element located by the given locator with Allure reporting
- `type_text(locator, text)`: Types text into an input field, clearing it first, with Allure reporting
- `get_text(locator)`: Returns the text content of an element located by the given locator

### LoginPage Class (`pages/login_page.py`)
The `LoginPage` class extends `BasePage` and encapsulates the login page functionality:
- `load()`: Loads the login page by navigating to the base URL
- `login(username, password)`: Performs the login action by entering username and password, then clicking the login button. Decorated with Allure step reporting
- `get_error_message()`: Retrieves and returns the text of any error message displayed on the login page

### InventoryPage Class (`pages/inventory_page.py`)
The `InventoryPage` class extends `BasePage` and encapsulates the inventory/products page functionality:
- `add_to_cart(product_name)`: Adds a specific product to the shopping cart by clicking its "Add to Cart" button. Uses the dynamic locator from `InventoryLocators.get_add_to_cart_btn()`. Decorated with Allure step reporting
- `get_cart_count()`: Retrieves and returns the current item count displayed in the shopping cart badge. Decorated with Allure step reporting

### TestLogin Class (`tests/test_login.py`)
The `TestLogin` class contains test methods for login functionality:
- `test_login_ddt(driver, data)`: Parameterized test method that performs login scenarios using data-driven testing. It loads the login page, performs login with provided credentials, and asserts the result based on the scenario (valid login checks URL contains "inventory", invalid login checks error message). Uses Allure for feature and story reporting

### TestInventory Class (`tests/test_inventory.py`)
The `TestInventory` class contains test methods for inventory/shopping cart functionality:
- `setup(driver)`: Pytest fixture with autouse that automatically logs in as a standard user before each test
- `test_add_product(driver, data)`: Parameterized test method that adds a product to the cart and asserts that the cart badge shows the expected count. Uses Allure for feature and story reporting

## Test Data

The project uses JSON files for test data:
- `login_data.json`: Contains test cases for login scenarios (valid/invalid credentials)
- `users.json`: Contains user credentials for different user roles
- `inventory_data.json`: Contains product names and expected cart badge values for inventory tests

## Configuration and Execution

- `pytest.ini`: Pytest configuration file
- `requirements.txt`: Python dependencies
- Tests can be run with `pytest` command
- Allure reports are generated in the `allure-results/` directory
- Browser configuration is handled in `conftest.py` with Chrome WebDriver management

## Dependencies

- Selenium WebDriver
- Pytest
- Webdriver Manager
- Allure Pytest</content>
<parameter name="filePath">/home/kacper/Documents/POM Selenium/README.md