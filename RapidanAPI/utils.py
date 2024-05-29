import json
from datetime import datetime
from fastapi import HTTPException

def load_api_keys():
    with open('api_keys.json', 'r+') as keys_file:
        return json.load(keys_file)

def update_api_keys(api_keys):
    with open('api_keys.json', 'w') as keys_file:
        json.dump(api_keys, keys_file)

def check_api_key(key, endpoint):
    api_keys = load_api_keys()

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
    update_api_keys(api_keys)
    return api_keys
