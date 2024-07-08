import requests
import pandas as pd

BASE_URL = "https://iue4h9npc6.execute-api.us-east-1.amazonaws.com/test/"

def global_oil_balance(api_key, balance_date, columns):
    url = f"{BASE_URL}global_oil_balance"
    headers = {
        'x-api-key': api_key
    }
    params = {
        'balance_date': balance_date,
        'columns': columns
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        response.raise_for_status()

def energy_calendar(api_key):
    url = f"{BASE_URL}energy_calendar"
    headers = {
        'x-api-key': api_key
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        response.raise_for_status()

def refined_products_module(api_key):
    url = f"{BASE_URL}refined_products_module"
    headers = {
        'x-api-key': api_key
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        response.raise_for_status()
