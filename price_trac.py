import os
import requests
from dotenv  import load_dotenv
from bs4 import BeautifulSoup
from pymongo import MongoClient

load_dotenv()
connection_string=os.getenv('connection_string')
client = MongoClient(connection_string)

db=client.prices
usd_collection=db.USD_INR
gold_collection=db.GOLD


def insert_into_db(collection,post:dict):
    _id = collection.insert_one(post).inserted_id
    print(_id)


def price_trace(item,save_data=True):
    try:
        url='https://www.google.com/finance/quote/'+item
        response = requests.get(url)

        if response.status_code==200:
            soup=BeautifulSoup(response.content,'html.parser')
            # print(soup) 
            for data in soup.findAll("div",attrs={"class","YMlKec fxKbKc"}):
                print(data.text)
                p=data.text

            for data in soup.findAll("div",attrs={"class","ygUjEc"}):
                d=data.text.split('·')[0]
                
                day=d.split(',')[0]
                    
                t=d.split(',')[1]  
                # print(day,t)

            p=float(p.replace('$','').replace(',',''))

            post={'price':p,
                'day':day,
                'time':t
                }
            print(post)
            if save_data:
                if item=='USD-INR':
                    insert_into_db(usd_collection,post)
                elif item=='GCW00:COMEX':
                    insert_into_db(gold_collection,post)

            return {'price':p,'day':day,'time':t}


    except Exception as e: 
        print(e)
            


