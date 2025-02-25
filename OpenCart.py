
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class OpenCart():

    def __init__(self, driver):
        self.driver = driver
        driver.get('https://www.opencart.com/')
        driver.maximize_window()
        print('OpenCart page opened')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login'))).click()
        print('Login page opened')
        time.sleep(40)


    def logIn(self):
        #self.driver.find_element(By.XPATH, '//input[@placeholder="Email"]').seld_keys('ffbfbfbfbfb')
        #self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('hdhdhdh')
        #self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        pass

    
        