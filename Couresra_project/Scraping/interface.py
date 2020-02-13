
# coding: utf-8

# In[10]:


from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import time
from Mongo_DB_interface import Mongo_db 
from utills import Navigate

class coursera(object):
    def __init__(self  ):
        pass
    def openn(self , url ):
        print("welcome to my project")
        profile = webdriver.FirefoxProfile()
        profile.set_preference('geo.enabled', False)
        profile.set_preference('geo.provider.use_corelocation', False)
        profile.set_preference('geo.prompt.testing', False)
        profile.set_preference('geo.prompt.testing.allow', False)
        self.url = url
        self.driver = webdriver.Firefox(firefox_profile=profile ,executable_path=r'C:\Users\dell\bin\geckodriver.exe')
        self.mong_obj = Mongo_db()
        self.my_db = self.mong_obj.connect_mongo_db("coursera_courses")
        self.my_collection = self.mong_obj.create_collection( self.my_db , "courses_info")
        self.navigat_obj = Navigate()
        self.dict = {}
    def nav_pages(self):
        python_button = self.driver.find_element_by_id("pagination_right_arrow_button")
        click = python_button.click()
        self.url = self.driver.current_url
    
    def close_driver(self):
        #To close the Driver
        self.driver.close()
    def search(self):
        self.driver.get( self.url )
        time.sleep( 10 )
        all_courses = self.driver.find_elements_by_xpath( '//li[@class = "ais-InfiniteHits-item"]' )
        for course in all_courses :
            title = self.navigat_obj.get_title( course )
            rating = self.navigat_obj.get_ratings( course )
            course_type = self.navigat_obj.get_course_type( course )
            level = self.navigat_obj.get_course_level(course)
            course_type = course_type.strip()
            link = self.navigat_obj.get_link( course )
            skills = self.navigat_obj.get_course_skills( link )
            if skills == "none" :
                skills = title.split(' ')
            #print ( title , rating , course_type  , level  , link , '\n' , skills )
            self.dict = {
                "course_title":title,
                "course_rating":rating,
                "course_type":course_type,
                "course_level":level,
                "skills" : skills,
                "link" : link
            }
            self.mong_obj.insert_document(self.my_collection , self.dict)
            
            
        
    
    
        
    
        

