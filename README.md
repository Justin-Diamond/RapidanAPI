# RapidanAPI allows our clients to conveniently pull energy data.

The RapidanAPI package can be installed with "pip install RapidanAPI".

Once this package is installed, various Rapidan datasets can be accessed with just a few lines of code and an API key. By changing the "endpoints" and "parameters", you can modify which dataset and columns of data will be pulled by your python script.

{% seo %} {% include head-custom.html %}
{% highlight python %}
from RapidanAPI import global_oil_balance

# API key, balance ID, and columns are passed as parameters
rapidan_api_key = "RAPIDAN_rapidan_api_key"
balance_id = "2306"
columns = "Balance"

# Get the data
df = global_oil_balance(rapidan_api_key, balance_id, columns)

# df is a pandas DataFrame containing the data
print(df)

# Output a csv file
df.to_csv("output.csv")
{% endhighlight %}

This code outputs the following dataframe:

{% seo %} {% include head-custom.html %}
{% highlight python %}
   Quarter (2306)  OECD Consumption (mb/d)  ...  WTI Forecast ($)  Brent-WTI Spread ($)
0            1Q20                45.501849  ...         48.000000              4.000000
1            2Q20                37.501710  ...         31.000000              4.000000
2            3Q20                42.238852  ...         40.890000              2.020000
3            4Q20                42.901522  ...         42.690000              2.570000
4            1Q21                42.512663  ...         58.140000              3.180000
5            2Q21                44.030264  ...         66.100000              1.980000
6            3Q21                45.742705  ...         70.500000              2.730000
7            4Q21                46.854999  ...         77.100000              2.560000
8            1Q22                45.838050  ...         95.000000              2.900000
9            2Q22                45.404778  ...        105.520000              6.450000
10           3Q22                46.622823  ...         91.430000              6.270000
11           4Q22                45.936485  ...         82.640000              5.990000
12           1Q23                45.211192  ...         75.980000              6.180000
13           2Q23                45.598498  ...         74.303148              3.983519
14           3Q23                47.041830  ...         86.000000              4.000000
15           4Q23                46.922884  ...         92.000000              5.000000
16           1Q24                46.572982  ...         85.000000              5.000000
17           2Q24                46.488073  ...         86.000000              4.000000
18           3Q24                47.367586  ...         91.000000              4.000000
19           4Q24                47.386866  ...         96.000000              4.000000
{% endhighlight %}

Endpoints have at most 3 parameters: rapidan_rapidan_api_key, date, and columns. The "tail" of endpoints such as "global_oil_balance" and "energy_calendar" refers to the last word in the endpoint. For example, the "tail" of "global_oil_balance" is just "balance".

# API key parameter (The "Who")
The "rapidan_rapidan_api_key" parameter contains your api key, which is used to identify you as a leigitmate user and can be set as a secret variable.

Endpoints like "energy_calendar" ONLY have this parameter, meaning the current, entire calendar is always pulled.

# Date parameter (The "When")
This parameter changes the date of the data,

The first part of the "date" parameter's name is the tail of the endpoint being used. For example, the date parameter's name for the "global_oil_balance" endpoint is "balance_date".

If this parameter is set to be "Current", the most up-to-date dataset will always be pulled. To get older versions of Rapidan datasets, this parameter should be set as a 4 digit number reflecting the year and month of the historical data being pulled. For example, setting the id parameter as 2307 will pull data from July 2023, and setting it as 2401 will pull data from January 2024.

# Columns parameter (The "What")
This parameter affects what columns will be pulled from the dataset.

When the "columns" parameter is set as the "tail" for the endpoint, the entire dataset will be pulled. For example, when the "global_oil_balance" endpoint" is used, setting this parameter as "balance" will pull the entire balance. To pull specific columns of data, this parameter can be set with a unique identifier, or multiple unique IDs separated by commas. For example, the parameter can be set as "OECD_CONS, OECD_SUPP" to pull only the OECD consumption and supply from our global oil balance.

Please refer to the dictionary called "uniqueIDs.json" on our GitHub page to see which identifiers correspond to different columns of data. 

# Rate limits and obtaining API keys
Each user is currently limited to 1500 API calls per month. However, the rate limit can be reset or modified upon request. Please reach out to Rapidan Energy Group for access to an API key.
