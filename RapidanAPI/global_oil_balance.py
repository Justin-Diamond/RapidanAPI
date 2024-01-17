import requests
import pandas as pd

def get_gob_data(api_key, balance_id, columns):
    url = f"https://rapidan-api-sabineleffler.replit.app/get_data/{api_key}/{balance_id}/{columns}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")
