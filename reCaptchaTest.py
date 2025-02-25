from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver  = webdriver.Chrome()
driver.get('https://google.com/recaptcha/api2/demo')
time.sleep(5)


#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'recaptcha-checkbox-border'))).click()
#print('Checkbox clicked')

#recaptcha_iframe = driver.find_element(By.XPATH, "//iframe[@title='reCAPTCHA']")#

##driver.switch_to.frame(recaptcha_iframe)
##recaptcha_checkbox = driver.find_element(By.ID, "recaptcha-anchor")
#recaptcha_checkbox.click()
#driver.switch_to.default_content()



submit = driver.find_element(By.ID, 'recaptcha-demo-submit')
submit.click()
print('Submit clicked')

time.sleep(10)
