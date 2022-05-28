from urllib import response
from matplotlib.pyplot import title
from selenium import webdriver
import json, time
from urllib.request import urlopen


f1 = open(r"C:\Users\pc\Desktop\pythonPrathmesh\Project-List\Bitly-Filter\Description.txt", mode='r+')

driver = webdriver.Chrome()
newSym = "+"
for i in f1:
    print(i)
    newLink = i + newSym
    # driver.maximize_window()  
    driver.get(newLink)
    title = driver.find_element_by_class_name("item-detail--title")
    print(title)
    time.sleep(3)

# driver.close()