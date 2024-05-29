import pandas as pd
import numpy as np
from fastapi import HTTPException
import asyncio
from main import check_api_key, load_api_keys

async def get_data_async(api_key: str):
    check_api_key(api_key, "energy_calendar")

    csv_file_path = 'calendar.csv'

    try:
        df = pd.read_csv(csv_file_path)
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.dropna(inplace=True)
        return df
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

def get_data(api_key: str):
    return asyncio.run(get_data_async(api_key))
