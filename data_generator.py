import schedule
import time
import requests

def get_data():
    try:
        url='http://127.0.0.1:8000/getprice/USD-INR'
        response = requests.get(url)

        print(response)

        url='http://127.0.0.1:8000/getprice/GCW00%3ACOMEX'
        response= requests.get(url)

        print(response)

    except Exception as e:
        print(e)


schedule.every(5).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(1)
