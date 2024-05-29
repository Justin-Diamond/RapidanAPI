import pandas as pd
import json
import os
from datetime import datetime
from fastapi import HTTPException
import asyncio
from .utils import check_api_key

async def get_data_async(api_keys, api_key: str, balance_date: str, columns: str):
    check_api_key(api_keys, api_key, "global_oil_balance")

    datetime_now = datetime.now()

    if balance_date.lower() == "current":
        current_year = datetime_now.year % 100
        current_month = datetime_now.month

        while True:
            balance_date = f'{current_year}{current_month:02d}'
            csv_file_path = f'{balance_date}_balance.csv'

            if os.path.isfile(csv_file_path):
                break

            current_month -= 1
            if current_month == 0:
                current_month = 12
                current_year -= 1
    else:
        csv_file_path = f'{balance_date}_balance.csv'

    try:
        df = pd.read_csv(csv_file_path, index_col="Quarter")
        df.index.name = f'{df.index.name} ({balance_date})'
        with open('uniqueIDs.json') as ids:
            unique_ids = json.load(ids)

        columns = [column.strip().lower() for column in columns.split(',')]
        if 'all' not in columns:
            if all(column.lower() in (key.lower() for key in unique_ids) for column in columns):
                column_names = [unique_ids[key] for key, value in unique_ids.items() if key.lower() in columns]
                if all(column_name in df.columns for column_name in column_names):
                    df = df.loc[:, column_names]
                else:
                    raise HTTPException(status_code=404, detail="Column not found")
            else:
                raise HTTPException(status_code=400, detail="Invalid parameter")
        return df
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
