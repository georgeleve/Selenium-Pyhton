# Georgios Gerasimos Leventopoulos
# Visit www.gmail.com and login to your email.
from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
driver.get("https://www.gmail.com")

driver.find_element_by_name("identifier").send_keys("yourgmail@gmail.com")  # gmail 
driver.find_element_by_xpath("//*[@id='identifierNext']/div/span/span").click()     # next
#problem here , google doesn't let me type my password
time.sleep(2)
driver.find_element_by_name("password").send_keys("yourpassword")           # password
driver.find_element_by_xpath("//*[@id='passwordNext']/div/span/span").click() # next
