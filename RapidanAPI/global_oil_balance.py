import requests
import pandas as pd

def global_oil_balance(api_key, balance_date, columns):
    url = f"https://rapidan-api-sabineleffler.replit.app/global_oil_balance/{api_key}/{balance_date}/{columns}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception("Failed to fetch data.")
