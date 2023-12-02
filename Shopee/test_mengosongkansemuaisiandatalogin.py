# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestMengosongkansemuaisiandatalogin():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_mengosongkansemuaisiandatalogin(self):
    # Test name: Mengosongkan semua isian data login
    # Step # | name | target | value
    # 1 | open | /buyer/login?next=https%3A%2F%2Fshopee.co.id%2Flog.in. | 
    self.driver.get("https://shopee.co.id/buyer/login?next=https%3A%2F%2Fshopee.co.id%2Flog.in.")
    # 2 | setWindowSize | 656x680 | 
    self.driver.set_window_size(656, 680)
    # 3 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | click | name=loginKey | 
    self.driver.find_element(By.NAME, "loginKey").click()
  
