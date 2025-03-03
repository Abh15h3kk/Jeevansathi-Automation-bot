import time
import os
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from dotenv import load_dotenv

load_dotenv()

EXCLUDED_OCCUPATIONS = [item.strip() for item in os.getenv("EXCLUDED_OCCUPATIONS", "").split(",") if item.strip()]
ALLOWED_OCCUPATION_PREFIXES = [item.strip() for item in os.getenv("ALLOWED_OCCUPATION_PREFIXES", "").split(",") if item.strip()]
ALLOWED_OCCUPATION_KEYWORDS = [item.strip() for item in os.getenv("ALLOWED_OCCUPATION_KEYWORDS", "").split(",") if item.strip()]

def process_profiles(driver, message):
    """
    Processes profiles on the page: filters profiles based on dynamic occupation criteria and sends messages.
    """
    processed_profiles = set()

    while True:
        profiles = driver.find_elements(By.CSS_SELECTOR, 'div[id^="custom-card-"]')
        print(f"Found {len(profiles)} profiles on page")

        for index, profile in enumerate(profiles):
            try:
                profile_id = profile.get_attribute("id").split("custom-card-")[1]
            except Exception as e:
                print(f"Error retrieving profile id for profile {index+1}: {str(e)}")
                continue

            if profile_id in processed_profiles:
                continue

            processed_profiles.add(profile_id)

            try:
                # Evaluate occupation criteria.
                try:
                    occupation = profile.find_element(By.ID, "occupation")
                    occ_text = occupation.text.strip()

                    # Exclude specific occupations dynamically.
                    if any(excluded in occ_text for excluded in EXCLUDED_OCCUPATIONS):
                        print(f"Skipping profile {index+1} (ID: {profile_id}): Excluded occupation")
                        continue

                    # Check if occupation starts with allowed prefixes or contains allowed keywords.
                    if not (occ_text.startswith(tuple(ALLOWED_OCCUPATION_PREFIXES)) or 
                            any(keyword in occ_text for keyword in ALLOWED_OCCUPATION_KEYWORDS)):
                        print(f"Skipping profile {index+1} (ID: {profile_id}): Occupation does not match")
                        continue

                except NoSuchElementException:
                    print(f"Profile {index+1} (ID: {profile_id}): Occupation element not found - skipping")
                    continue

                # Scroll profile into view.
                driver.execute_script("arguments[0].scrollIntoView(true);", profile)
                time.sleep(1)
                
                button_id = f"INITIATE-{profile_id}"
                try:
                    interest_button = WebDriverWait(profile, 10).until(
                        EC.element_to_be_clickable((By.ID, button_id))
                    )
                except (TimeoutException, NoSuchElementException):
                    print(f"Profile {index+1} (ID: {profile_id}): Interest button not found - skipping")
                    continue

                print(f"Processing profile {index+1} with ID: {profile_id}")
                interest_button.click()
                time.sleep(3)
                
                message_input_id = f"sendMessageInput-{profile_id}"
                send_button_id = f"sendMessageButton-{profile_id}"
                
                try:
                    message_input = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.ID, message_input_id))
                    )
                    message_input.send_keys(message)
                    
                    send_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.ID, send_button_id))
                    )
                    send_button.click()
                    print("Message sent successfully")
                    time.sleep(4)
                except Exception as e:
                    print(f"Error sending message for profile {index+1} (ID: {profile_id}): {str(e)}")
            except Exception as e:
                print(f"Error processing profile {index+1} (ID: {profile_id}): {str(e)}")
                continue

        # Scroll to load more profiles.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        try:
            older_matches_button = driver.find_element(By.ID, "primary-button")
            if older_matches_button.is_displayed():
                print("Found 'View older matches' button. Clicking to load more profiles...")
                older_matches_button.click()
                time.sleep(3)
        except NoSuchElementException:
            pass

        updated_profiles = driver.find_elements(By.CSS_SELECTOR, 'div[id^="custom-card-"]')
        if len(updated_profiles) <= len(processed_profiles):
            print("No new profiles loaded. Waiting for 1 minute before closing the browser...")
            time.sleep(60)
            break
