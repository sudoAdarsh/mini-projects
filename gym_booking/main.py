import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options

GYM_URL = "https://appbrewery.github.io/gym/"
EMAIL = "adarsh@test.com"
PASSWORD = "heyitzme"
NAME = "Adarsh Upadhyay"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

# WebDriverWait(driver, timeout=2)

# login_button = driver.find_element(By.ID, value="login-button")
# login_button.click()

# email = driver.find_element(By.NAME, value="email")
# email.send_keys(EMAIL)

# password = driver.find_element(By.NAME, value="password")
# password.send_keys(PASSWORD)

# submit_button = driver.find_element(By.ID, value="submit-button")
# submit_button.click()