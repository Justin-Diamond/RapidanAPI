import httpx

async def global_oil_balance(api_key, balance_id, columns):
    url = f"https://rapidan-api-sabineleffler.replit.app/global_oil_balance/{api_key}/{balance_id}/{columns}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    response.raise_for_status()  # Ensure we raise an exception for HTTP errors
    return response.json()
