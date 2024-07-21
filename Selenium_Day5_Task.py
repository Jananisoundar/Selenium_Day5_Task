from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_saucedemo_login_logout():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Open the website
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)  # Adding a small delay to ensure the page loads properly

        # Capture cookies before login
        cookies_before_login = driver.get_cookies()
        print("Cookies before login:", cookies_before_login)

        # Fill in the login form
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)  # Allow time for the login process to complete

        # Capture cookies after login
        cookies_after_login = driver.get_cookies()
        print("Cookies after login:", cookies_after_login)

        # Verify if cookies were generated during login
        cookies_before_login_set = {cookie['name'] for cookie in cookies_before_login}
        cookies_after_login_set = {cookie['name'] for cookie in cookies_after_login}

        new_cookies = cookies_after_login_set - cookies_before_login_set
        if new_cookies:
            print("New cookies generated during login:")
            for cookie_name in new_cookies:
                print(cookie_name)
        else:
            print("No new cookies were generated during login.")

        # Perform logout
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(2)  # Allow time for the logout process to complete

    finally:
        # Close the browser window
        driver.quit()


# Run the function to test
test_saucedemo_login_logout()
