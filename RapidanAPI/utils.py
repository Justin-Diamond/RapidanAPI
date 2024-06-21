import json
from datetime import datetime
from fastapi import HTTPException
from replit.object_storage import Client

client = Client()

def load_api_keys():
    api_keys_text = client.download_as_text('api_keys.json')
    return json.loads(api_keys_text)

def check_api_key(api_keys, key, endpoint):
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

def update_api_key_count(api_keys, key):
    api_keys[key]['count'] += 1
