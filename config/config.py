import os

class Config:
    BASE_URL = "https://www.saucedemo.com/"
    TIMEOUT = 10  # Seconds
    BROWSER = "chrome"  # options: chrome, firefox, edge
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "True"