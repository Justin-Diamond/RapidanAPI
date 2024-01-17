# RapidanAPI: Insights made convenient.
Welcome to RapidanAPI! We hope this tool will help our clients automatically process the data and forecasts we work so hard to create each day. We're confident in the value that our weekly calendars, monthly balances, and other datasets provide – and we know that lots of good people depend on them. That's why we've made it our mission to get as much energy market wisdom into your hands as conveniently and quickly as possible.

Right now, RapidanAPI is in the early stages of development, but we plan on regularly expanding the number of endpoints and datasets that are available. If you have any questions about RapidanAPI or need help with its implementation, don't hesitate to reach out.

# Getting started with RapidanAPI
The RapidanAPI package can be installed with "pip install RapidanAPI".

Once this package is installed, various Rapidan datasets can be accessed with just a few lines of code and an API key. By changing the "endpoints" and "parameters", you can modify the datasets and columns that are being pulled by your python script – which should look something like this:

{% seo %} {% include head-custom.html %}
{% highlight python %}
from RapidanAPI import global_oil_balance

# API key, balance ID, and columns are passed as parameters
rapidan_api_key = "RAPIDAN_API_KEY"
balance_id = "2306"
columns = "All"

# Get the data
df = global_oil_balance(rapidan_api_key, balance_id, columns)

# df is a pandas DataFrame containing the data
print(df)

# Output a csv file
df.to_csv("output.csv")
{% endhighlight %}

This outputs a table that can be saved as a .csv, .xls, or other file:

{% seo %} {% include head-custom.html %}
{% highlight html %}
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

Endpoints have at most 3 parameters: rapidan_api_key, date, and columns.

# API key parameter (The "Who")
The "rapidan_api_key" parameter contains your api key, which is used to identify you as a leigitmate user and can be set as a secret variable. You can reach out to Rapidan Energy Group at any time to inquire about API key access.

Endpoints like "energy_calendar" ONLY require this parameter, since all calendar pulls yield the most current & complete calendar available, by default. Here's an example of how you can pull energy calendar data using only this parameter:

{% seo %} {% include head-custom.html %}
{% highlight python %}
from RapidanAPI import energy_calendar

# API key is passed as a parameter
rapidan_api_key = "RAPIDAN_API_KEY"

# Get the data
df = energy_calendar(rapidan_api_key)

# df is a pandas DataFrame containing the calendar
print(df)

# Output a csv file
df.to_csv("calendar.csv")
{% endhighlight %}

Each api key is currently limited to 1500 API calls per month. However, the rate limit can be reset or modified upon request.

# Date parameter (The "When")
The "date" parameter's name will depend on the last word of the endpoint being used. For example, the date parameter's name for the "global_oil_balance" endpoint is "balance_date".

If this parameter is set to "Current", the most up-to-date dataset available will be pulled. To get older versions of Rapidan datasets, this parameter should be set as a 4 digit number reflecting the year and month of the historical data being pulled (YYMM). For example, setting the date parameter as 2307 will pull data from July 2023, and setting it as 2401 will pull data from January 2024.

# Columns parameter (The "What")
When the "columns" parameter is set to "All" for this endpoint, the entire dataset will be pulled. To pull specific columns of data, this parameter can be set to a unique identifier, or multiple unique IDs separated by commas. For example, the parameter can be set as "OECD_CONS, OECD_SUPP" to pull only the OECD consumption and supply from our global oil balance.

Here is a list of unique IDs which correspond to different columns of data in our global oil balance:

<div style="font-size: 8px;">
{% seo %} {% include head-custom.html %}
{% highlight json %}
{
    "OECD_CONS": "OECD Consumption (mb/d)",
    "OECD_USA_CONS": "United States Consumption (mb/d)",
    "OECD_JAP_CONS": "Japan Consumption (mb/d)",
    "OECD_CAN_CONS": "Canada Consumption (mb/d)",
    "OECD_EUR_CONS": "Europe Consumption (mb/d)",
    "OECD_OTH_CONS": "Other OECD Consumption (mb/d)",
    "NONOECD_CONS": "Non-OECD Consumption (mb/d)",
    "NONOECD_CHN_CONS": "China Consumption (mb/d)",
    "NONOECD_IND_CONS": "India Consumption (mb/d)",
    "NONOECD_BRA_CONS": "Brazil Consumption (mb/d)",
    "NONOECD_RUS_CONS": "Russia Consumption (mb/d)",
    "NONOECD_OTH_CONS": "Other Non-OECD Consumption (mb/d)",
    "TOT_CONS": "Total World Consumption",
    "OECD_SUPP": "OECD Supply (mb/d)",
    "OECD_USA_SUPP_TL": "U.S. Total Liquids Supply (mb/d)",
    "OECD_USA_SUPP_CR": "Crude Supply (mb/d)",
    "OECD_USA_SUPP_CR_LOW48": "Lower 48 Supply (mb/d)",
    "OECD_USA_SUPP_CR_GOM": "GOM Supply (mb/d)",
    "OECD_USA_SUPP_CR_AL": "Alaska Supply (mb/d)",
    "OECD_USA_SUPP_NGL": "NGLs Supply (mb/d)",
    "OECD_USA_SUPP_OL": "Other US Liquids Supply (mb/d)",
    "OECD_MEX_SUPP": "Mexico Supply (mb/d)",
    "OECD_CAN_SUPP": "Canada Supply (mb/d)",
    "OECD_OTH_SUPP": "Other OECD Supply (mb/d)",
    "NONOECD_SUPP": "Non-OECD Supply (mb/d)",
    "NONOECD_BRA_SUPP": "Brazil Supply (mb/d)",
    "NONOECD_CHN_SUPP": "China Supply (mb/d)",
    "NONOECD_RUS_SUPP": "Russia Supply (mb/d)",
    "NONOECD_RUS_SUPP_CR": "Russia Crude Supply (mb/d)",
    "NONOECD_OTH_SUPP": "Other Non-OECD Supply (mb/d)",
    "NONOPEC_SUPP": "Non-OPEC Supply Supply (mb/d)",
    "OPEC_SUPP": "OPEC Supply (mb/d)",
    "OPEC_SUPP_CR": "Crude Oil Portion Supply (mb/d)",
    "OPEC_SUPP_OL": "Other Liquids Supply (mb/d)",
    "TOT_SUPP": "Total World Supply (mb/d)",
    "SURPLUS": "Implied Surplus (mb/d)",
    "OECD_IND_STK_CHNG": "OECD Industry Stock Change (mb/d)",
    "OECD_USA_IND_STK_CHNG": "US Industry Stocks (Ex. SPR) (mb/d)",
    "OECD_OTH_IND_STK_CHNG": "Other OECD Industry Stocks (mb/d)",
    "OTH_STK_CHNG": "Other Stock Change* (mb/d)",
    "NONOECD_CHN_STK_CHNG": "Chinese Crude Stocks (mb/d)",
    "OECD_SPR_STK_CHNG": "OECD SPR (mb/d)",
    "TOT_OOW_CHNG": "Oil on Water (mb/d)",
    "NONOECD_OTH_STK_CHNG": "Other Non-OECD Stocks (mb/d)",
    "OPEC_SPARECAP": "OPEC Spare Capacity (mb/d)",
    "BRENT_PRICE": "Brent Forecast ($)",
    "WTI_PRICE": "WTI Forecast ($)",
    "BRENT_WTI_SPREAD": "Brent-WTI Spread ($)"
}
{% endhighlight %}
</div>

# Data releases
Now that you're familiar with the API, you're probably wondering when to run these scripts. If you're automating them, it's important to know which dates to run them on. 

The weekly energy calendar is updated on Sunday evening each week (which gives API users a day-long headstart on calendar access), and the global oil balance will be updated per the following publication schedule:

- Monday, January 22, 2024

- Tuesday, February 20, 2024

- Monday, March 18, 2024

- Monday, April 15, 2024

- Friday, May 17, 2024

- Friday, June 14, 2024

- Monday, July 15, 2024

- Thursday, August 15, 2024

- Monday, September 16, 2024

- Thursday, October 17, 2024

- Monday, November 18, 2024

- Monday, December 16, 2024

# Conclusion
As mentioned above, RapidanAPI is in its early stages of development, but we plan on regularly expanding the number of endpoints and datasets that are available. If you have any questions about RapidanAPI or need help with its implementation, don't hesitate to reach out.
