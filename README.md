
# Bitcoin Price Predctions Web App



# Key Features

1 -Historical Data Fetching: The application fetches historical Bitcoin price data from the CryptoCompare API. This data is used to train the machine learning model.

2- Price Prediction: The trained model is used to predict future Bitcoin prices. Users can input the number of days ahead for which they want to predict the price, and the application will display the predicted price.

3- Current Price Display: The application also provides the current price of Bitcoin in USD, fetched from the CoinGecko API.

4- Data Caching: To reduce the number of API calls and improve performance, the application caches the historical data for a day. If the data is already cached and is less than a day old, the application will use the cached data instead of making a new API call.

5- User-Friendly Interface: The application has a simple, intuitive user interface where users can input the number of days for which they want to predict the price and view the predicted price.

6- Error Handling: The application includes basic error handling to manage situations where the API calls fail or the data is not available.

# Purpose

The purpose of this application is to provide users with a tool to predict the future price of Bitcoin based on historical data. It is intended for educational purposes and should not be used for actual trading or investment decisions

# Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

# Installation

Step-by-step instructions on how to get your project up and running.

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
```

2. Navigate to the project directory:

```bash
cd your-repo
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Set up any environment variables or configuration files.

# Usage

Instructions on how to use your project. This could include how to run the application, how to interact with it, and any other relevant information.
don't forget to replace the Api with your "CryptoCompare" Api

```bash
python app.py
```
The app will be running on: http://127.0.0.1:5000/

# Deployment

Still working on; and trying to make a server to host my flask application

# Contributing

Feel free to do anything.

# Demo video on LinkedIn

Your contact information, such as your email address, or links to your social media profiles or website.

