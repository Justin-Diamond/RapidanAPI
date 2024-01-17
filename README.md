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

This code outputs the following dataframe:

{% seo %} {% include head-custom.html %}
{% highlight python %}
   Quarter (2311)  OECD Consumption (mb/d)  ...  WTI Forecast ($)  Brent-WTI Spread ($)
0            1Q20                45.484306  ...            48.000                 4.000
1            2Q20                37.531423  ...            31.000                 4.000
2            3Q20                42.295335  ...            40.890                 2.020
3            4Q20                42.956560  ...            42.690                 2.570
4            1Q21                42.573695  ...            58.140                 3.180
5            2Q21                44.070292  ...            66.100                 1.980
6            3Q21                45.789515  ...            70.500                 2.730
7            4Q21                46.904131  ...            77.100                 2.560
8            1Q22                45.767426  ...            95.000                 2.900
9            2Q22                45.277626  ...           105.520                 6.450
10           3Q22                46.218934  ...            91.430                 6.270
11           4Q22                45.783839  ...            82.640                 5.990
12           1Q23                45.457402  ...            75.980                 6.180
13           2Q23                45.709023  ...            73.670                 4.050
14           3Q23                46.009247  ...            82.217                 3.703
15           4Q23                46.129017  ...            84.000                 5.000
16           1Q24                45.812430  ...            85.000                 5.000
17           2Q24                45.567691  ...            86.000                 4.000
18           3Q24                46.128759  ...            83.000                 4.000
19           4Q24                46.394244  ...            85.000                 4.000
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
