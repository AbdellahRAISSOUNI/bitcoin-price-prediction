from flask import Flask, request, render_template, jsonify
import requests
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from cache import load_cache, save_cache
from pycoingecko import CoinGeckoAPI


app = Flask(__name__)
cg = CoinGeckoAPI()

# Replace 'YOUR_API_KEY' with your actual CryptoCompare API key
API_KEY = 'bae9d03705e886e9e3814bc359c57b593f02afedec91a873df00b53bed4ad685'
SYMBOL = 'BTC'
CURRENCY = 'USD'
LIMIT = 365  # Number of days of data to fetch

# Fetch historical Bitcoin price data
def fetch_historical_data(api_key, symbol, currency, limit):
    cached_data = load_cache()
    if cached_data is not None:
        return cached_data

    url = f"https://min-api.cryptocompare.com/data/v2/histoday"
    params = {
        'fsym': symbol,
        'tsym': currency,
        'limit': limit,
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    save_cache(data)
    return data

# Preprocess the data
def preprocess_data(data):
    df = pd.DataFrame(data['Data']['Data'])
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True)
    df.sort_index(inplace=True)
    df['day_of_year'] = df.index.dayofyear
    return df

# Train the model
def train_model(df):
    model = LinearRegression()
    X = df.index.to_series().diff().dt.days.fillna(0).astype(int).values.reshape(-1, 1)
    y = df['close'].values.reshape(-1, 1)
    scaler_x = MinMaxScaler()
    scaler_y = MinMaxScaler()
    X_scaled = scaler_x.fit_transform(X)
    y_scaled = scaler_y.fit_transform(y)
    model.fit(X_scaled, y_scaled)
    return model, scaler_x, scaler_y

# Fetch and preprocess data
historical_data = fetch_historical_data(API_KEY, SYMBOL, CURRENCY, LIMIT)
df = preprocess_data(historical_data)
model, scaler_x, scaler_y = train_model(df)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get the input from the form
        days_ahead = int(request.form.get('days_ahead'))
        
        # Make a prediction
        last_date = df.index[-1]
        future_dates = pd.date_range(start=last_date, periods=days_ahead + 1, freq='D')[1:]
        future_X = np.array(range(len(df), len(df) + days_ahead)).reshape(-1, 1)
        future_X_scaled = scaler_x.transform(future_X)
        future_predictions_scaled = model.predict(future_X_scaled)
        future_predictions = scaler_y.inverse_transform(future_predictions_scaled)
        
        prediction = pd.Series(future_predictions.flatten(), index=future_dates)
        
    return render_template('index.html', prediction=prediction)

@app.route('/current_price', methods=['GET'])
def current_price():
    # Fetch the current price of Bitcoin in USD
    response = cg.get_price(ids='bitcoin', vs_currencies='usd')
    current_price = response['bitcoin']['usd']
    return jsonify({'price': current_price})

if __name__ == '__main__':
    app.run(debug=True)