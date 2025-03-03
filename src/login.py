from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform_login(driver, url, email, password):
    """
    Navigates to the website and performs login using the provided credentials.

    Parameters:
        driver: Selenium WebDriver instance.
        url: URL of the website.
        email: Login email.
        password: Login password.

    Returns:
        bool: True if login was successful, False otherwise.
    """
    driver.get(url)
    try:
        # Click the login button.
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-attr="LoginNav"]'))
        )
        login_button.click()
        
        # Wait for the login fields.
        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div#EmailContainer input"))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div#PasswordContainer input"))
        )
        
        email_field.send_keys(email)
        password_field.send_keys(password)
        
        login_submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "jspcLoginLayerButton"))
        )
        login_submit_button.click()
        return True

    except Exception as e:
        print(f"Login failed: {str(e)}")
        return False