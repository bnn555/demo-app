
# Import libraries
from flask import Flask, render_template
import json
import requests
import threading
import datetime
import os
  

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# # defining key/request url
# price = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
# avg = "https://api.binance.com/api/v3/ticker?symbol=BTCUSDT&windowSize=10m"

# def getBTCPrice():
#     # requesting data from url
#     BTCprice = requests.get(price)  
#     BTCprice = BTCprice.json()
#     BTCavg = requests.get(avg)  
#     BTCavg = BTCavg.json()
#     now = datetime.datetime.now()
#     print(f"at {now} {BTCprice['symbol']} price is {BTCprice['price']} avg price for last 10 minutes is {BTCavg['weightedAvgPrice']}")


# def getAVGPrice():
#     # requesting data from url
#     data = requests.get(avg)  
#     data = data.json()
#     now = datetime.datetime.now()
#     print(f"at {now} {data['symbol']} price is {data['price']}")
#     # threading.Timer(10.0, getBTCPrice).start()

# def main():
#     getBTCPrice()

if __name__ == "__main__":
    port = int(os.environ.get('APP_PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)