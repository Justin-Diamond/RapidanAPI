import httpx

async def energy_calendar(api_key):
    url = f"https://rapidan-api-sabineleffler.replit.app/calendar/{api_key}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    response.raise_for_status()  # Ensure we raise an exception for HTTP errors
    return response.json()
