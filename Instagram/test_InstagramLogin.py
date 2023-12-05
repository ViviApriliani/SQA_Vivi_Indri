from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

# Fungsi untuk login ke Instagram
def login_instagram(driver, username, password):
    driver.get("https://www.instagram.com")
    username_field = driver.find_element("id", "email")
    password_field = driver.find_element("id", "pass")
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    

# Informasi login Instagram
username = "Your_username"
password = "your_password"

# Buat instance WebDriver
driver = webdriver.Chrome()

# Login ke Instagram
login_instagram(driver, username, password)

# Menutup browser
driver.close()
