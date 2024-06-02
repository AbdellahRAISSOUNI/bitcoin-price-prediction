import requests
import pandas as pd

def fetch_historical_data(api_key, symbol, limit):
    url = f"https://min-api.cryptocompare.com/data/v2/histoday"
    params = {
        'fsym': symbol,
        'tsym': 'USD',
        'limit': limit,
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

# Replace 'YOUR_API_KEY' with your actual CryptoCompare API key
api_key = 'bae9d03705e886e9e3814bc359c57b593f02afedec91a873df00b53bed4ad685'
symbol = 'BTC'
limit = 100  # Number of days of data to fetch

historical_data = fetch_historical_data(api_key, symbol, limit)