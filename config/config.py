import os  # <--- Don't forget me!

class Config:
    BASE_URL = "https://www.saucedemo.com/"
    TIMEOUT = 10
    BROWSER = "chrome"
    
    # The Robot looks for "HEADLESS" in the cloud. 
    # If it finds it, it turns invisible. If not, it stays visible.
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"