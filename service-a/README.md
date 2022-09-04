# service-a

Service-a is a simple webserver created with python and flask.  
His main objective is to serve a webpage that presents the current BTC price and the average BTC price for last 10 minutes at each 10 seconds.  
In order to achieve this goal we are using flask to serve a simple html page that has some javascript functions that queery [binance public API](https://binance-docs.github.io/apidocs/spot/en/#symbol-price-ticker) every 10 seconds for the required information.  
The API that where used are:  
1. [symbol-price-ticker](https://binance-docs.github.io/apidocs/spot/en/#symbol-price-ticker)  
2. [rolling window price change statistics](https://binance-docs.github.io/apidocs/spot/en/#rolling-window-price-change-statistics) with an rolling window of 10 minutes.  

The app has been packed inside a docker container using this [Dockerfile](Dockerfile).