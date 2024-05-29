import requests
import pandas as pd

def get_gob_data(api_key, balance_id, columns):
    url = f"https://rapidan-api-sabineleffler.replit.app/global_oil_balance/{api_key}/{balance_id}/{columns}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Inspect the structure of the data
        if isinstance(data, dict):
            # If the data is a dictionary of scalar values
            if all(isinstance(value, (int, float, str)) for value in data.values()):
                data = [data]  # Convert to a list of records

        try:
            df = pd.DataFrame(data)
        except ValueError as e:
            print(f"Error creating DataFrame: {e}")
            raise

        return df
    else:
        raise Exception("Failed to fetch data.")
