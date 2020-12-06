# Georgios Gerasimos Leventopoulos
# Login into netflix using facebook account
from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
driver.get("https://www.netflix.com/")

driver.find_element_by_xpath("//*[@id='cookie-disclosure']/div/button/span[1]").click()  # close cookie window
time.sleep(1)
driver.find_element_by_xpath("//*[@id='appMountPoint']/div/div/div/div/div/div[1]/div[2]/a").click() # click Sign In
time.sleep(1)
driver.find_element_by_xpath("//*[@id='appMountPoint']/div/div[3]/div/div/div[2]/form/div/div/button").click() #click Sign in with facebook
time.sleep(1)

driver.switch_to_window(driver.window_handles[1]) # switch window
driver.find_element_by_name("email").send_keys("yourgmail@gmail.com") # type email
time.sleep(1)
driver.find_element_by_name("pass").send_keys("yourpassword") # type password
driver.find_element_by_name("login").click() # click login

#driver.switch_to_window(driver.window_handles[1]) # switch window
#driver.find_element_by_name("__CONFIRM__").click() # click continue as "facebook name"
