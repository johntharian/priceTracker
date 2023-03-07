import os
import requests
from dotenv  import load_dotenv
from bs4 import BeautifulSoup
from pymongo import MongoClient


class DataBase():
    def __init__(self) -> None: 
        load_dotenv()
        connection_string=os.getenv('connection_string')
        client = MongoClient(connection_string)

        db=client.prices
        self.collection=db.USD_INR


    def insert_into_db(self,post:dict):
        _id = self.collection.insert_one(post).inserted_id
        print(_id)

def price_trace():

    try:
        url='https://www.google.com/finance/quote/USD-INR'
        response = requests.get(url)

        if response.status_code==200:
            soup=BeautifulSoup(response.content,'html.parser')

            for data in soup.findAll("div",attrs={"class","YMlKec fxKbKc"}):
                print(data.text)
                p=data.text

            for data in soup.findAll("div",attrs={"class","ygUjEc"}):
                d=data.text.split('·')[0]
                
                day=d.split(',')[0]
                
                t=d.split(',')[1]  
                print(day,t)


            post={'price':p,
                'day':day,
                'time':t
                }
            
            db=DataBase()

            db.insert_into_db(post)
            # collection.insert_one(post)

    except Exception as e: 
        print(e)
        

            

price_trace()
