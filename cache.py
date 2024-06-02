# cache.py
import os
import pickle
from datetime import datetime, timedelta

CACHE_FILE = 'historical_data.pkl'
CACHE_EXPIRY = timedelta(days=1)  # Cache expires after 1 day

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'rb') as f:
            cache_data = pickle.load(f)
            last_updated = cache_data['last_updated']
            if datetime.now() - last_updated < CACHE_EXPIRY:
                return cache_data['data']
    return None

def save_cache(data):
    cache_data = {
        'last_updated': datetime.now(),
        'data': data
    }
    with open(CACHE_FILE, 'wb') as f:
        pickle.dump(cache_data, f)