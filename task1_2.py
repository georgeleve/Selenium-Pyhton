# Georgios Gerasimos Leventopoulos csd4152
from selenium import webdriver
import time
import pickle
import json

def save_cookies(driver, location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))

driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
driver.get("https://www.ebay.com")
save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies2.txt") # save cookies
time.sleep(1)

# MACBOOK PRO
driver.find_element_by_name("_nkw").send_keys("macbook pro") # write in search bar
driver.find_element_by_id("gh-btn").click()                  # click search
time.sleep(1)
driver.find_element_by_xpath("//*[@id='srp-river-results']/ul/li[1]/div/div[2]/a/h3").click() # click on 1st element
save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies2.txt") # save cookies
print(driver.get_cookies())
driver.save_screenshot("macbook_pro1.png") # screenshot
driver.back() # back
time.sleep(1)
driver.find_element_by_xpath("//*[@id='srp-river-results']/ul/li[2]/div/div[2]/a/h3/span").click() # click on 3rd element
save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies2.txt") # save cookies
print(driver.get_cookies())
driver.save_screenshot("macbook_pro2.png")
driver.back()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='srp-river-results']/ul/li[3]/div/div[2]/a/h3").click() # click on 2nd element
save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies2.txt") # save cookies
driver.save_screenshot("macbook_pro3.png")
driver.back()
driver.back() # go back to search bar

# DELL XPS
driver.find_element_by_name("_nkw").send_keys("dell xps")  
driver.find_element_by_id("gh-btn").click()

driver.find_element_by_xpath("//*[@id='srp-river-results']/ul/li[1]/div/div[2]/a/h3").click() 
save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies2.txt") # save cookies
driver.save_screenshot("dell_xps1.png")
driver.back()

driver.find_element_by_xpath("//*[@id='srp-river-results']/ul/li[2]/div/div[2]/a/h3").click()
save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies2.txt") # save cookies
driver.save_screenshot("dell_xps2.png")
driver.back()

driver.find_element_by_xpath("//*[@id='srp-river-results']/ul/li[3]/div/div[2]/a/h3").click()
save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies2.txt") # save cookies
driver.save_screenshot("dell_xps3.png")
driver.back()
driver.back() 

# NIKE SHOES
driver.find_element_by_name("_nkw").send_keys("nike shoes")
driver.find_element_by_id("gh-btn").click()

driver.find_element_by_xpath("//*[@id='srp-river-results']/ul/li[1]/div/div[2]/a/h3").click() 
save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies2.txt") # save cookies
driver.save_screenshot("nike_shoes1.png")
driver.back()

driver.find_element_by_xpath("//*[@id='srp-river-results']/ul/li[2]/div/div[2]/a/h3").click()
save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies2.txt") # save cookies 
driver.save_screenshot("nike_shoes2.png")
driver.back()

driver.find_element_by_xpath("//*[@id='srp-river-results']/ul/li[3]/div/div[2]/a/h3").click() 
save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies2.txt") # save cookies
driver.save_screenshot("nike_shoes3.png")
driver.back()
driver.back()

# MELLER GLASSES
driver.find_element_by_name("_nkw").send_keys("meller glasses")
driver.find_element_by_id("gh-btn").click()
time.sleep(1)

driver.find_element_by_xpath("//*[@id='srp-river-results']/ul/li[1]/div/div[2]/a").click()
save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies2.txt") # save cookies
driver.save_screenshot("meller_glasses1.png")
driver.back()

driver.find_element_by_xpath("//*[@id='srp-river-results']/ul/li[2]/div/div[2]/a/h3").click() 
save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies2.txt") # save cookies
driver.save_screenshot("meller_glasses2.png")
driver.back()

driver.find_element_by_xpath("//*[@id='srp-river-results']/ul/li[3]/div/div[2]/a/h3").click() 
save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies2.txt") # save cookies
driver.save_screenshot("meller_glasses3.png")
driver.back()
driver.back()