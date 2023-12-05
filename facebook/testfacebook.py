from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Fungsi untuk login ke Facebook
def login_facebook(driver, username, password):
    driver.get("https://www.facebook.com")
    time.sleep(5)
    username_field = driver.find_element("id", "email")
    password_field = driver.find_element("id", "pass")
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(20)

# Informasi login Facebook
username = "Your_username"
password = "your_password"

# Buat instance WebDriver
driver = webdriver.Chrome()

# Login ke Facebook
login_facebook(driver, username, password)

# Menutup browser
driver.close()
