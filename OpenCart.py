
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class OpenCart():

    def __init__(self, driver):
        self.driver = driver
        driver.get('https://www.opencart.com/index.php?route=common/home/login')
        driver.maximize_window()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login'))).click()
        time.sleep(30)

        

    def logIn(self):
        #self.driver.find_element(By.XPATH, '//input[@placeholder="Email"]').seld_keys('ffbfbfbfbfb')
        #self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('hdhdhdh')
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()


    
        