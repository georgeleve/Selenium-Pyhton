# Georgios Gerasimos Leventopoulos csd4152 
# Visit www.facebook.com and login to your facebook account.
from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
driver.get("https://www.facebook.com")

driver.find_element_by_name("email").send_keys("george.george5000@gmail.com") # email
time.sleep(1) # stop for 1sec
driver.find_element_by_name("pass").send_keys("password#31") # password
time.sleep(1) 
driver.find_element_by_xpath("//*[@id='u_0_d']").click() # click login
