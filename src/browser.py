from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
    """
    Create and return a Chrome WebDriver instance with configured options.
    """
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    return driver
