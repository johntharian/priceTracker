from fastapi import FastAPI

from price_trac import price_trace

app=FastAPI()

@app.get('/')
async def root():
    return {"Status":"OK"}

@app.get('/getprice')
async def getprice():
    return price_trace(save_data=True)

@app.get('/admin-getprice')
async def admingetprice():
    return price_trace(save_data=False)

@app.get('/getFullData')
async def getFullData():
    return {}


