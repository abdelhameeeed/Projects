
# coding: utf-8

# In[ ]:
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

class Navigate(object):
    def __init__( self  ):
        pass 
    
    def get_title(self , course_sel):
        try:
            return course_sel.find_element_by_class_name("color-primary-text").text
        except:
            return "none"
    
    def get_ratings(self , course_sel):
        try :
            return course_sel.find_element_by_class_name("ratings-text").text 
        except :
            return "none"
    
    def get_course_type(self , course_sel):
        try:
            return course_sel.find_element_by_class_name("product-type-row").text
        except :
            return "none"
    
    def get_course_level(self , course_sel):
        try:
            return course_sel.find_element_by_class_name("product-difficulty").text
        except:
            return "none"
    
    def get_course_skills( self , link_):
        try:
            data_req = requests.get(link_)
            data_txt = data_req.text
            data_soup = BeautifulSoup(data_txt , "html.parser")
            all_skills = data_soup.find("div" , {"class" : "Box_120drhm-o_O-displayflex_poyjc-o_O-wrap_rmgg7w"})
            skills = []
            for skill in all_skills:
                skills.append(skill.span.span.text)
                #print(skill.span.span.text)
            return skills 
        except:
            return "none"
    def get_link( self , course_sel):
        try:
            return course_sel.find_element_by_class_name("rc-DesktopSearchCard").get_attribute("href")
        except:
            return "none"

