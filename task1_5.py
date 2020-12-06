# Georgios Gerasimos Leventopoulos

# 0 minute, 4 times a day, for 5 days, in August, whatever day  (using crontab)
# crontab -e      
# 0 0,6,12,18 1,2,3 1 0 python3 task1_5.py >> task1_5.out
# tail -f task1_5.out
from selenium import webdriver
import selenium.webdriver
import requests
import pickle
import pprint
import json
import time

def save_cookies(driver, location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))

driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")

#login
driver.get("https://www.news.gr/") #1
time.sleep(2)
driver.find_element_by_xpath("//*[@id='qc-cmp2-ui']/div[2]/div/button[3]").click() #accept cookies
time.sleep(1)
driver.find_element_by_xpath("//*[@id='content-container']/div[1]/header/div[1]/div/div[2]/div[1]/div[1]/div[2]/a[1]").click()
time.sleep(1)
driver.find_element_by_name("email").send_keys("yourgmail@gmail.com")
driver.find_element_by_name("password").send_keys("yourpassword")
driver.find_element_by_xpath("//*[@id='nb-popup-login']/div[2]/div[4]/div[2]/form/div[4]").click()
time.sleep(1)            

mylist = [] 
elems = driver.find_elements_by_xpath("//a[@href]")   #store links
#put the links inside the list
for elem in elems:
    print(elem.get_attribute("href"))
    mylist.append(elem.get_attribute("href"))
# traverse list to visit 20 random links 
i = 45
while i < 65:
    driver.get(mylist[i])
    save_cookies(driver, "C:\\yourpath\\cookies.txt")
    time.sleep(2)
    i += 1

#print("1st crawl : 40 trackers") 
#2nd crawl : 5 new trackers: a.com,b.com,d.com… 
#Do you see any change in the volume of trackers?
#Do you observe new domains?Why do they change?
