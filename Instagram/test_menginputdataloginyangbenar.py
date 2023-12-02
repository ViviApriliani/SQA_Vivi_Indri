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

class TestMenginputdataloginyangbenar():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_menginputdataloginyangbenar(self):
    # Test name: Menginput data login yang benar
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.instagram.com/")
    # 2 | setWindowSize | 656x680 | 
    self.driver.set_window_size(656, 680)
    # 3 | click | name=username | 
    self.driver.find_element(By.NAME, "username").click()
    # 4 | type | name=username | Siapaaku8455
    self.driver.find_element(By.NAME, "username").send_keys("Siapaaku8455")
    # 5 | click | name=password | 
    self.driver.find_element(By.NAME, "password").click()
    # 6 | type | name=password | Katasandisaatini8455!
    self.driver.find_element(By.NAME, "password").send_keys("Katasandisaatini8455!")
    # 7 | click | css=.\_acan > .x9f619 | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_acan > .x9f619").click()
    # 8 | click | css=.xjqpnuy | 
    self.driver.find_element(By.CSS_SELECTOR, ".xjqpnuy").click()
    # 9 | click | css=.\_a9_1 | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_a9_1").click()
  
