import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config.config import Config

@pytest.fixture(scope="function")
def driver():
    # Setup
    options = webdriver.ChromeOptions()
    prefs = {
        # 1. Disable "Save Password" bubble
        "credentials_enable_service": False,
        
        # 2. Disable "Password Manager" entirely
        "profile.password_manager_enabled": False,
        
        # 3. Disable "Change Password" warning (Leak Detection)
        "profile.password_manager_leak_detection": False,
        
        # (Optional) Disable "Restore pages?" popup after a crash
        "profile.exit_type": "Normal"
    }
    
    # Apply the preferences
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-extensions")       # Disables all 3rd party extensions
    options.add_argument("--disable-popup-blocking")   # Prevents popup blocking
    options.add_argument("--disable-notifications")    # Blocks "Show notifications" prompts

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    if True:
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")              # Required for Linux/CI
        options.add_argument("--disable-dev-shm-usage")   # Overcome limited resource problems
        options.add_argument("--window-size=1920,1080")   # Prevent "element not visible" errors    
    # Automatically manages driver binary
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    
    yield driver
    
    # Teardown
    driver.quit()

# Hook to take screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )