# Georgios Gerasimos Leventopoulos
# Login into Netflix using email

from selenium import webdriver
import time
driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe") # find path
driver.get("https://www.netflix.com/")

driver.find_element_by_xpath("//*[@id='cookie-disclosure']/div/button/span[1]").click()  # close cookie window
time.sleep(1)
driver.find_element_by_xpath("//*[@id='appMountPoint']/div/div/div/div/div/div[1]/div[2]/a").click() # Sign In
time.sleep(1)
driver.find_element_by_name("userLoginId").send_keys("yourgmail@gmail.com") # email
time.sleep(1)
driver.find_element_by_name("password").send_keys("yourpassword") # password
driver.find_element_by_xpath("//*[@id='appMountPoint']/div/div[3]/div/div/div[1]/form/button").click() # Sing In
