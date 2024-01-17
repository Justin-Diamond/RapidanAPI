# RapidanAPI allows our clients to conveniently pull energy data.

The RapidanAPI package can be installed with "pip install RapidanAPI"

Once this package is installed, various Rapidan datasets can be accessed with just a few lines of code and an API key. By changing the "endpoints" and "parameters", you can modify which dataset and columns of data will be pulled by your python script.

{% seo %} {% include head-custom.html %}
{% highlight python %}
from RapidanAPI import global_oil_balance

# API key, balance ID, and columns are passed as parameters
api_key = "RAPIDAN_API_KEY"
balance_id = "2311"
columns = "Balance"

# Get the data
df = global_oil_balance(api_key, balance_id, columns)

# df is a pandas DataFrame containing the data
print(df)

# Output a csv file
df.to_csv("output.csv")
{% endhighlight %}

Endpoints will each have 3 parameters: api_key, id, and columns. The "tail" of endpoints such as "global_oil_balance" and "energy_calendar" refers to the last word in the endpoint. For example, the "tail" of "global_oil_balance" is just "balance".

# API key parameter
The "api_key" parameter contains your api_key, which can be set as a secret variable.

# ID parameter
The first part of the "id" parameter's name is the tail of the endpoint being used. For example, the id parameter's name for the "global_oil_balance" endpoint is "balance_id", and for the "energy_calendar" endpoint is "calendar_id". 

If this parameter is left empty, the most up-to-date dataset will always be pulled. To get older versions of Rapidan datasets, this parameter should be set as a 4 digit number reflecting the year and month of the historical data being pulled. For example, setting the id parameter as 2307 will pull data from July 2023, and setting it as 2401 will pull data from January 2024.

# Columns parameter
When the "columns" parameter is set as the "tail" for the endpoint, the entire dataset will be pulled. For example, when the "global_oil_balance" endpoint" is used, setting this parameter as "balance" will pull the entire balance. To pull specific columns of data, this parameter can be set as a unique identifier, or as multiple unique IDs separated by commas. For example, the parameter can be set as "OECD_CONS, OECD_SUPP" to pull only the OECD consumption and supply from our global oil balance. 

Please refer to the dictionary called "uniqueIDs.json" on our GitHub page to see which identifiers correspond to different columns of data.

# Rate limits and obtaining API keys
Each user is currently limited to 1500 API calls per month. However, the rate limit can be reset or modified upon request. Please reach out to Rapidan Energy Group for access to an API key.
