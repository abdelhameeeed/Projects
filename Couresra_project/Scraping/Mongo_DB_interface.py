
# coding: utf-8

# In[5]:


from pymongo import MongoClient


# In[6]:


class Mongo_db(object):
    def __init__(self):
        pass
    
    def connect_mongo_db( self , db_name ):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[db_name]
        return self.db
    def create_collection( self , db , collection):
        self.collectionn = db.collection
        return self.collectionn
    def insert_document(self , collection , document):
        try :
            collection.insert_one(document)
            print("inserted is successfuly ... !!!!")
        except Exception as ex:
            print("can not insert in database ")
            print(ex)
            
        

