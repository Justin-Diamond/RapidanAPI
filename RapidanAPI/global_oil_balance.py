import requests
import pandas as pd

def get_gob_data(rapidan_api_key, balance_date, columns):
    url = f"https://rapidan-api-sabineleffler.replit.app/get_gob_data/{rapidan_api_key}/{balance_date}/{columns}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception("Failed to fetch data.")
