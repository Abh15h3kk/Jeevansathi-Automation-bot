import time
import os
import sys
from selenium.common.exceptions import WebDriverException
from browser import create_driver
from login import perform_login
from profile_processor import process_profiles

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config.credentials import EMAIL, PASSWORD, MESSAGE

def main():
    driver = create_driver()
    website_url = "https://www.jeevansathi.com/"

    try:
        if not perform_login(driver, website_url, EMAIL, PASSWORD):
            print("Login was unsuccessful. Exiting.")
            return

        # Wait for profiles to load.
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id^="custom-card-"]'))
        )

        process_profiles(driver, MESSAGE)

    except WebDriverException as e:
        print(f"Critical WebDriver error occurred: {str(e)}")
        print("Pausing execution for 1 minute for inspection.")
        time.sleep(60)

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    main()