import pandas as pd
import numpy as np
from fastapi import HTTPException
import json
from .utils import check_api_key

def get_data(api_key: str):
    api_keys = load_api_keys()  # Load API keys

    check_api_key(api_keys, api_key, "energy_calendar")

    csv_file_path = 'calendar.csv'

    try:
        df = pd.read_csv(csv_file_path)
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.dropna(inplace=True)
        return df
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

def load_api_keys():
    with open('api_keys.json') as f:
        return json.load(f)
