from OpenCart import OpenCart
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



try:
    driver = webdriver.Chrome()
    Main = OpenCart(driver)
    Main.logIn()

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
 




