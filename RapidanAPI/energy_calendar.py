import pandas as pd
import numpy as np
from fastapi import HTTPException

async def get_data():
    csv_file_path = 'calendar.csv'

    try:
        df = pd.read_csv(csv_file_path)
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.dropna(inplace=True)
        return df
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
