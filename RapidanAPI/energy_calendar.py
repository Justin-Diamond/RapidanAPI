import pandas as pd
import numpy as np
from fastapi import HTTPException
import asyncio

async def get_data_async():
    csv_file_path = 'calendar.csv'

    try:
        df = pd.read_csv(csv_file_path)
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.dropna(inplace=True)
        return df
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

def get_data():
    return asyncio.run(get_data_async())
