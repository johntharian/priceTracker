import os
from dotenv  import load_dotenv

from pymongo import MongoClient

load_dotenv()
connection_string=os.getenv('connection_string')
client = MongoClient(connection_string)

db=client.prices
usd_collection=db.USD_INR
gold_collection=db.GOLD

def reset_db():
    r= usd_collection.delete_many({})
    print(r.deleted_count)

    r= gold_collection.delete_many({})
    print(r.deleted_count)

    print("deleted all")

    return "reset db"