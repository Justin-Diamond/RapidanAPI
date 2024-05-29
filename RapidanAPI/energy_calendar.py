import requests
import pandas as pd

def get_ec_data(api_key):
    url = f"https://rapidan-api-sabineleffler.replit.app/calendar/{api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)  # Print the data to understand its structure

        # Check if the data is a dictionary of scalars
        if isinstance(data, dict):
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
