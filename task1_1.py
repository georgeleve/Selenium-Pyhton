# Georgios Gerasimos Leventopoulos csd4152

# (1) store all cookies to a cookie.out file
# (2) store all http traffic to a json output (hint : browsermob proxy, mitmproxy)
# (3) store all the visited pages to html form.
# Parse the json output and save to file.
# Total pages = 10

from selenium import webdriver
import selenium.webdriver
import requests
import pickle
import json
import time

def save_cookies(driver, location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.cnn.gr/")            

mylist = [] 
elems = driver.find_elements_by_xpath("//a[@href]")
#put in the list
for elem in elems:
    print(elem.get_attribute("href"))
    mylist.append(elem.get_attribute("href"))

#print(mylist[5:15])
# visit 10 random links 
i = 5
while i < 15:
    driver.get(mylist[i])
    save_cookies(driver, "C:\\Users\\leven\\Desktop\\Python\\cookies.txt")
    time.sleep(2)
    i += 1

# json examples: 
# some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
# y = json.loads(x)

# the result is a Python dictionary:
# print(y["age"])