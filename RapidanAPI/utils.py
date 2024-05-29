import json
from datetime import datetime
from fastapi import HTTPException
from replit import web
from replit.object_storage import Client

client = Client()

def load_api_keys():
    try:
        # Download the API keys from Replit's object storage
        contents = client.download_as_text("api_keys.json")
        return json.loads(contents)
    except Exception as e:
        print(f"Error loading API keys: {e}")
        return {}

def update_api_keys(api_keys):
    try:
        # Upload the API keys to Replit's object storage
        contents = json.dumps(api_keys)
        client.upload_from_text("api_keys.json", contents)
    except Exception as e:
        print(f"Error updating API keys: {e}")

def check_api_key(key, endpoint):
    api_keys = load_api_keys()

    if key not in api_keys:
        raise HTTPException(status_code=401, detail="Unauthorized")

    if endpoint.lower() not in (ep.lower() for ep in api_keys[key]['endpoints']):
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
