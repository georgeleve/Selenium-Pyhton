# Georgios Gerasimos Leventopoulos csd4152

# 0 minute, three times a day, for 5 days, in September, whatever day  (using crontab)
# crontab -e
# 0 0,8,16 1-5 8 * /usr/bin/python3 task2.py >> task2.out
# tail -f test.out

# 15 domains and 10 sublinks for each domain
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
domains = ['https://www.news247.gr/', 'https://www.sport24.gr/','https://www.csd.uoc.gr/','https://www.newsbomb.gr/'
'https://www.uoc.gr/','https://www.ntua.gr/en/','https://www.stanford.edu/', 'https://www.harvard.edu/']
mylist = []


#1
#login
driver.get("https://www.news.gr/") 
time.sleep(2)
driver.find_element_by_xpath("//*[@id='qc-cmp2-ui']/div[2]/div/button[3]").click() #accept cookies
time.sleep(1)
driver.find_element_by_xpath("//*[@id='content-container']/div[1]/header/div[1]/div/div[2]/div[1]/div[1]/div[2]/a[1]").click()
time.sleep(1)
driver.find_element_by_name("email").send_keys("george.george5000@gmail.com")
driver.find_element_by_name("password").send_keys("george12345")
driver.find_element_by_xpath("//*[@id='nb-popup-login']/div[2]/div[4]/div[2]/form/div[4]").click()
time.sleep(1)             
elems = driver.find_elements_by_xpath("//a[@href]")   #store links
#put the links in the list
for elem in elems:
    print(elem.get_attribute("href"))
    mylist.append(elem.get_attribute("href"))
# visit 10 random sublinks 
i = 45
while i < 55:
    driver.get(mylist[i])
    save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies.txt")
    time.sleep(2)
    i += 1


#2 
mylist[:] = []  #clear list
driver.get("https://www.hackerrank.com/") 
time.sleep(1) # Login
driver.find_element_by_xpath("//*[@id='menu-item-2887']/a").click()   
time.sleep(1)
driver.find_element_by_xpath("//*[@id='post-175']/div/div/div[1]/div/div/div[2]/div[2]/div/div[4]/div/div/a/span").click()
time.sleep(1)
driver.find_element_by_id("input-1").send_keys("leventopoulos.george@gmail.com") # email
driver.find_element_by_id("input-2").send_keys("george@#18") # password
driver.find_element_by_xpath("//*[@id='content']/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/form/div[4]/button").click()
time.sleep(2)
elems = driver.find_elements_by_xpath("//a[@href]")   #store links
for elem in elems:
    print(elem.get_attribute("href"))
    mylist.append(elem.get_attribute("href"))
i = 2
while i < 12:
    driver.get(mylist[i])
    save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies.txt")
    time.sleep(2)
    i += 1


#3
mylist[:] = []  #clear list
driver.get("https://leetcode.com/")   
time.sleep(1)   
driver.find_element_by_xpath("//*[@id='landing-page-app']/div/div[1]/div[3]/div[1]/div/div/div[2]/div/a[5]/span").click()
time.sleep(1)
driver.find_element_by_name("login").send_keys("georgeleve") # email
time.sleep(1)
driver.find_element_by_name("password").send_keys("Jn}TJ5R@") # password
time.sleep(1)
driver.find_element_by_xpath("//*[@id='signin_btn']/div").click()
time.sleep(3)
elems = driver.find_elements_by_xpath("//a[@href]")   #store links
for elem in elems:
    print(elem.get_attribute("href"))
    mylist.append(elem.get_attribute("href"))

i = 2
while i < 12:
    driver.get(mylist[i])
    time.sleep(2)
    save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies.txt")
    i += 1


#4
mylist[:] = []  #clear list
driver.get("https://www.happydeals.gr/") 
time.sleep(2)
driver.find_element_by_xpath("//*[@id='simplemodal-container']/a").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='header']/div/div[3]/ul/li[1]/a").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='login-email-address']").send_keys("george.george5000@gmail.com") # email
driver.find_element_by_name("password").send_keys("polihappydeals") # password
driver.find_element_by_xpath("//*[@id='repass-form']/div[4]/div/button").click()
time.sleep(2)
elems = driver.find_elements_by_xpath("//a[@href]")   #store links
for elem in elems:
    print(elem.get_attribute("href"))
    mylist.append(elem.get_attribute("href"))
i = 10
while i < 20:
    driver.get(mylist[i])
    time.sleep(2)
    save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies.txt")
    i += 1


#5
mylist[:] = []  #clear list
driver.get("https://www.usnews.com/")  
time.sleep(1)
driver.find_element_by_id("gdpr-modal-agree").click() # click agree
time.sleep(2)
elems = driver.find_elements_by_xpath("//a[@href]")   #store links
for elem in elems:
    print(elem.get_attribute("href"))
    mylist.append(elem.get_attribute("href")) 
i = 45
while i < 55:
    driver.get(mylist[i])
    save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies.txt")
    i += 1


#6
mylist[:] = []  #clear list
driver.get("https://www.cnn.gr/")            
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    print(elem.get_attribute("href"))
    mylist.append(elem.get_attribute("href"))
i = 5
while i < 15:
    driver.get(mylist[i])
    save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies.txt")
    i += 1


#7 #8, #9, #10, #11, #12, #13, #14, #15

for i in range(len(domains)):
    mylist[:] = []  #clear list
    driver.get(domains[i])  
    elems = driver.find_elements_by_xpath("//a[@href]") #store links
    #put the links in the list
    for elem in elems:
        print(elem.get_attribute("href"))
        mylist.append(elem.get_attribute("href"))
    i = 20
    # visit 10 random sublinks
    while i < 31:
        driver.get(mylist[i])
        save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies.txt")
        #time.sleep(2)
        i += 1



# How does a domain understands that a bot/crawler does the requests?
#Depending on the amount of content on each page or the number of pages on the site, it could be in the website operator's 
#best interests not to allow search indexing too often, since too much indexing could overtax the server, drive up bandwidth costs, or both.