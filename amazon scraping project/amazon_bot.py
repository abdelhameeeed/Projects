
# coding: utf-8

# In[1]:


import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time


# In[ ]:


class amazon(object):
    def __init__(self , items):
        self.amazon_url = "https://www.amazon.ca"
        self.items = items 
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\dell\bin\geckodriver.exe')
    def  search_item(self):
        urls =[]
        price = []
        name = []
        self.driver.get( self.amazon_url )
        time.sleep(2)
        for i in self.items :
            print("searching for items " , i )
            search_bos = self.driver.find_element_by_id("twotabsearchtextbox")
            search_bos.send_keys(i)
            click_button = self.driver.find_element_by_class_name("nav-input")
            click_button.click()
            time.sleep(2)
            first_item = self.driver.find_element_by_xpath('//div[@class="sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 AdHolder sg-col sg-col-4-of-20 sg-col-4-of-32"]')
            n = self.get_product_name(first_item)
            p = self.get_product_price(first_item)
            l = self.get_product_link(first_item)
            urls.append(l)
            name.append(n)
            price.append(p)
            self.driver.find_element_by_id("twotabsearchtextbox").clear()
        return name , price , urls 
    
    def get_product_name(self , sel_obj):
        return sel_obj.find_element_by_class_name("a-size-base-plus").text
        
    def get_product_link(self , sel_obj):
        return sel_obj.find_element_by_class_name("a-link-normal").get_attribute("href")
    
    
    def get_product_price(self , sel_obj):
        return sel_obj.find_element_by_class_name("a-price").text
        
    

