import requests
import pandas as pd

def get_ec_data(api_key):
    url = f"https://rapidan-api-sabineleffler.replit.app/get_data/{api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception("Failed to fetch data.")
