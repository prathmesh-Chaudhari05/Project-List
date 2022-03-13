from selenium import webdriver
import json, time

f1 = open(r"C:\Users\pc\Desktop\pythonPrathmesh\Project-List\Bitly-Filter\Description.txt", mode='r+')
# print(f1.read())

driver = webdriver.Chrome()

for i in f1:
    newLink = i+"+"
    driver.maximize_window()  
    driver.get(newLink)

    # print(f1.readline(1))
    time.sleep(3)

driver.close()