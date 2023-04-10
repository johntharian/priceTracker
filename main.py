from fastapi import FastAPI

from price_trac import price_trace

app = FastAPI()

@app.get('/')
async def root():
    return {"Status":"OK"}

@app.get('/getprice/{item}')
def getprice(item):
    data= price_trace(item,save_data=True)
    return data

@app.get('/admin-getprice/{item}')
def admingetprice(item):
    return price_trace(item,save_data=False)

@app.get('/getFullData')
def getFullData():
    return {}


