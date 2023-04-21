import os
import numpy as np

import matplotlib.pyplot as plt
from pymongo import MongoClient
from dotenv  import load_dotenv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


load_dotenv()
connection_string=os.getenv('connection_string')
client = MongoClient(connection_string)

db=client.prices
usd_collection=db.USD_INR
gold_collection=db.GOLD


class Retrain:
    def __init__(self):
       self.o_count_usd=0
       self.o_count_g=0
       self.usd_inr_price=[]
       self.g_price=[]


    def usd_mongo_to_arr(self):
        count=usd_collection.count_documents({})
        print(count)
        print(self.o_count_usd)
        if count!=self.o_count_usd:
            self.o_count_usd=count
            price=usd_collection.find({})
            for data in price:
                self.usd_inr_price.append(data['price'])
            
            return self.usd_inr_price

    def g_mongo_to_arr(self):
        count=gold_collection.count_documents({})
        print(count)
        print(self.o_count_g)
        if count!=self.o_count_g:
            self.o_count_g=count
            price=gold_collection.find({})
            for data in price:
                self.g_price.append(data['price'])
                
            return self.g_price
            

    def check_new_entries(self):
        count=usd_collection.count_documents({})
        if self.o_count_g!=count:
            return True
    

    def train(self):
        if self.check_new_entries:
            usd_inr_price=self.usd_mongo_to_arr()
            g_price=self.g_mongo_to_arr()
            
            usd_inr_price=np.array(self.usd_inr_price).reshape(-1,1)

            print(len(usd_inr_price))
            x_train, x_test, y_train, y_test = train_test_split(usd_inr_price,self.g_price,test_size=0.25, random_state=42)
            m=LinearRegression()    
            m.fit(x_train, y_train)
            print(m.score(x_test,y_test))

            y_pred = m.predict(x_test)
            plt.scatter(x_test, y_test, color ='b')
            plt.plot(x_test, y_pred, color ='k')

            plt.show()

r=Retrain()

r.train()

