from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize webdriver
driver = webdriver.Chrome()

def login_instagram(username, password):
    driver.get("https://www.instagram.com/")
    time.sleep(2)

    # Enter username
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys(username)
    
    # Enter password
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    
    time.sleep(5)

def navigate_to_profile(target_username):
    driver.get(f"https://www.instagram.com/{target_username}/")
    time.sleep(3)

def check_violations():
    # Define violation keywords
    violations = {
        "HATE": ["devil", "666", "savage", "love", "hate", "followers", "selling", "sold", "seller", "dick", "ban", "banned", "free", "method", "paid"],
        "SELF": ["suicide", "blood", "death", "dead", "kill myself"],
        "BULLY": [],  # This will be checked in mentions
        "VIOLENT": ["hitler", "osama bin laden", "guns"],
        "Illegal(drugs)": ["drugs", "cocaine"],
        "Pretending": ["celebrity", "verified"],
        "NUDITY": ["nude", "sex", "send nudes"]
    }

    # Check bio
    bio = driver.find_element(By.XPATH, "//div[@class='-vDIg']/span").text
    check_text(bio, violations, "bio")

    # Check posts
    posts = driver.find_elements(By.XPATH, "//div[@class='v1Nh3 kIKUG  _bz0w']")
    for post in posts:
        post.click()
        time.sleep(2)
        post_text = driver.find_element(By.XPATH, "//div[@class='C4VMK']/span").text
        check_text(post_text, violations, "post")
        driver.find_element(By.XPATH, "//button[contains(text(),'Close')]").click()
        time.sleep(1)

    # Check story (if available)
    # Note: Checking stories is more complex as they require interaction with the UI elements dynamically

def check_text(text, violations, context):
    for category, keywords in violations.items():
        for keyword in keywords:
            if keyword in text.lower():
                print(f"Violation found in {context}: {category} - {keyword}")

def report_violation(reason):
    # Function to report the violation
    # This function would interact with the Instagram UI to report the account
    pass

# Usage
username = "your_username"
password = "your_password"
target_username = "target_account"

login_instagram(username, password)
navigate_to_profile(target_username)
check_violations()

driver.quit()
