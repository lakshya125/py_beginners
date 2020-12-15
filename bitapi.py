import requests as req
import time
now=time.ctime()

# Fetches BitCoin's Current Price
bit = req.get('https://api.coindesk.com/v1/bpi/currentprice.json')

print("1 Bitcoin is worth $" + bit.json()['bpi']['USD']['rate'] + " as of "+ now)
