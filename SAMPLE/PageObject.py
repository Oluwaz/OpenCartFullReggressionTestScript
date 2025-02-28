from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Aphonics():
    def __init__(self, driver):
        self.driver = driver
        driver.get('https://www.aphonicss.com/')
        driver.maximize_window()
        
    
    def NewArrivals(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable())
        pass
