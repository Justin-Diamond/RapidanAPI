import pandas as pd
import numpy as np
from fastapi import HTTPException
import asyncio

async def get_data_async(api_key: str):
    api_keys = load_api_keys()
    check_api_key(api_key, "energy_calendar", api_keys)

    csv_file_path = 'calendar.csv'

    try:
        df = pd.read_csv(csv_file_path)
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.dropna(inplace=True)
        return df
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

def get_data(api_key: str):
    return asyncio.run(get_data_async(api_key))

def load_api_keys():
    with open('api_keys.json', 'r+') as keys_file:
        return json.load(keys_file)

def check_api_key(key, endpoint, api_keys):
    if key not in api_keys:
        raise HTTPException(status_code=401, detail="Unauthorized")

    if endpoint not in api_keys[key]['endpoints']:
        raise HTTPException(status_code=403, detail="Forbidden")

    if api_keys[key]['count'] >= 1500:
        raise HTTPException(status_code=429, detail="API call limit reached")

    reset_date = datetime.strptime(api_keys[key]['reset_date'], '%Y-%m-%d')
    if reset_date.month != datetime.now().month or reset_date.year != datetime.now().year:
        api_keys[key]['count'] = 0
        api_keys[key]['reset_date'] = datetime.now().strftime('%Y-%m-%d')

    api_keys[key]['count'] += 1
    with open('api_keys.json', 'w') as keys_file:
        json.dump(api_keys, keys_file)
