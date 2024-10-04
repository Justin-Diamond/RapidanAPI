import requests
import pandas as pd

BASE_URL = "https://iue4h9npc6.execute-api.us-east-1.amazonaws.com/RapidanAPI/"

def global_oil_balance(api_key, balance_date, columns, frequency):
    url = f"{BASE_URL}global_oil_balance"
    headers = {
        'x-api-key': api_key
    }
    params = {
        'balance_date': balance_date,
        'columns': columns,
        'frequency': frequency
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

def china_risk_tracker(api_key):
    url = f"{BASE_URL}china_risk_tracker"
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

def us_gas_balance(api_key):
    url = f"{BASE_URL}us_gas_balance"
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

def eu_gas_balance(api_key):
    url = f"{BASE_URL}eu_gas_balance"
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

def refined_products_outlook(api_key):
    url = f"{BASE_URL}refined_products_outlook"
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

def barrels_at_risk(api_key):
    url = f"{BASE_URL}barrels_at_risk"
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
