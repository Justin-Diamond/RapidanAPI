# RapidanAPI: Insights made convenient.
Welcome to RapidanAPI! This Python Package helps Rapidan's clients process API-accessible data and forecasts as conveniently as possible.

RapidanAPI is currently in Version 1.1.1, but we’re already working to expand the number and extensiveness of datasets available through RapidanAPI. If you have any questions about RapidanAPI or need help with its implementation, don't hesitate to reach out.

# Getting started with RapidanAPI
The easiest way to install this package is to use the package installer for Python, which enables a simple "pip" command.

The RapidanAPI package can be installed with the command "pip install RapidanAPI" either on your own computer or in a virtual environment. Installation should only take a few seconds!

# Available Endpoints
Once this package is installed, you can access most datasets with a few lines of code and an API key – but endpoints like the Global Oil Balance have some extra parameters. Here is a list of endpoints and their parameters:

{% seo %} {% include head-custom.html %}
{% highlight html %}
Endpoint : Parameters

global_oil_balance : api_key, balance_date, columns
refined_products_module : api_key
china_risk_tracker : api_key
energy_calendar : api_key
us_gas_balance : api_key
eu_gas_balance : api_key
{% endhighlight %}

# API Keys
The "api_key" parameter contains your api key, which is used to identify you as a legitimate user and should be set as a secret variable. The default usage plan allows each key to make up to 3000 requests per month. You can reach out to Rapidan at any time to inquire about API key access. Endpoints which only require the API key parameter will always pulls the most current & complete version of the dataset. Here's how you can pull energy calendar data using only the “api_key” parameter:

{% seo %} {% include head-custom.html %}
{% highlight python %}
from RapidanAPI import energy_calendar

# API key is passed as a parameter
api_key = "API_KEY"

# Get the data
df = energy_calendar(api_key)

# df is a pandas DataFrame containing the calendar
print(df)

# Output a csv file
df.to_csv("Energy_Calendar.csv")
{% endhighlight %}

# Other Parameters
For datasets like the Global Oil Balance, parameters such as “balance_date” and “columns” are included to give you extra control of the data, and allow you to retrieve historical oil balances. In the future, we plan on adding these parameters to other endpoints – such as the refined products module and gas balance endpoints.

The “balance_date” parameter is in YYMM format, and includes our historical oil balances from 2301 (January 2023) to present. For example, setting the date parameter as 2307 will pull data from July 2023, and setting it as 2401 will pull data from January 2024. If you want to pull the most recently updated dataset, just set this parameter as balance_date="Current" or balance_date=None.

The “columns” parameter lets you pull specific columns of data. If you want to pull the entire dataset, just set this parameter as columns="All" or columns=None. But if you want to pull specific columns, just enter one or more of the column codes listed at the bottom of this page as comma separated values. For example, columns=“OECD_CONS, OECD_SUPP” will pull OECD consumption and OECD supply. Here’s how you can pull all of the columns from our June 2023 global oil balance:

{% seo %} {% include head-custom.html %}
{% highlight python %}
from RapidanAPI import global_oil_balance

# API key, balance ID, and columns are passed as parameters
api_key = "API_KEY"
balance_id = "2306"
columns = "All"

# Get the data
df = global_oil_balance(api_key, balance_id, columns)

# df is a pandas DataFrame containing the data
print(df)

# Output a csv file
df.to_csv("Global_Oil_Balance.csv")
{% endhighlight %}

This outputs a table that can be saved as a .csv, .xlsx, or other file:

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

# More Example Code
For your convenience, this section contains a few chunks of example code.

Here's a script that pulls and prints every dataframe available through RapidanAPI:

{% seo %} {% include head-custom.html %}
{% highlight python %}
from RapidanAPI import global_oil_balance, china_risk_tracker, refined_products_module, eu_gas_balance, us_gas_balance, energy_calendar
import pandas as pd

api_key = "YOUR_API_KEY"

# Pull data from each endpoint and store in a DataFrame
global_oil_balance_df = global_oil_balance(api_key, balance_date="Current", columns="All")
refined_products_df = refined_products_module(api_key)
china_risk_tracker_df = china_risk_tracker(api_key)
eu_gas_balance_df = eu_gas_balance(api_key)
us_gas_balance_df = us_gas_balance(api_key)
energy_calendar_df = energy_calendar(api_key)

# Print each DataFrame with combined text
print("Global Oil Balance DataFrame:\n", global_oil_balance_df.head(), "\n")
print("Refined Products Module DataFrame:\n", refined_products_df.head(), "\n")
print("China Risk Tracker DataFrame:\n", china_risk_tracker_df.head(), "\n")
print("EU Gas Balance DataFrame:\n", eu_gas_balance_df.head(), "\n")
print("US Gas Balance DataFrame:\n", us_gas_balance_df.head(), "\n")
print("Energy Calendar DataFrame:\n", energy_calendar_df.head(), "\n")
{% endhighlight %}

The following script uses the "openpyxl" package (which can be installed with the command "pip install openpyxl") to write all of the endpoints to an excel file called "Rapidan_Data.xlsx."

{% seo %} {% include head-custom.html %}
{% highlight python %}
from RapidanAPI import (global_oil_balance, china_risk_tracker, refined_products_module, eu_gas_balance, us_gas_balance, energy_calendar)
import pandas as pd

api_key = "YOUR_API_KEY"

with pd.ExcelWriter("Rapidan_Data.xlsx", engine="openpyxl") as writer:
    global_oil_balance(api_key, balance_date="Current", columns="All").to_excel(writer, sheet_name="Global_Oil_Balance", index=False)
    refined_products_module(api_key).to_excel(writer, sheet_name="Refined_Products", index=False)
    china_risk_tracker(api_key).to_excel(writer, sheet_name="China_Risk_Tracker", index=False)
    eu_gas_balance(api_key).to_excel(writer, sheet_name="EU_Gas_Balance", index=False)
    us_gas_balance(api_key).to_excel(writer, sheet_name="US_Gas_Balance", index=False)
    energy_calendar(api_key).to_excel(writer, sheet_name="Energy_Calendar", index=False)
{% endhighlight %}

Another option is to make charts in Python, right when you pull the data. Here's an example of a script that uses the "matplotlib" and "seaborn" packages, to create some good-looking charts based on the EU Gas Balance endpoint:

{% seo %} {% include head-custom.html %}
{% highlight python %}
from RapidanAPI import eu_gas_balance
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Your API key
api_key = "YOUR_API_KEY"

# Pull df from the EU gas balance module and process date column
df = eu_gas_balance(api_key)
date_column = df.columns[0]
df[date_column] = pd.to_datetime(df[date_column], format="%B-%y", errors="coerce")
df = df.dropna(subset=[date_column])

# Extract relevant columns
df = df[[date_column, "Total Production", "Total LNG Imports", "Total Pipeline Imports"]]

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(14, 8))
colors = ["#0b3d91", "#1f77b4", "#4a90e2"]
labels = ["Total Production", "Total LNG Imports", "Total Pipeline Imports"]
linestyles = ["-", "--", ":"]

for i, col in enumerate(labels):
    plt.plot(df[date_column], df[col], linestyle=linestyles[i], color=colors[i], label=col)

# Customize the plot
plt.title("Rapidan's EU Gas Balance", fontsize=20, weight="bold")
plt.xlabel("Date", fontsize=14, weight="bold")
plt.ylabel("Volume (bcm)", fontsize=14, weight="bold")
plt.legend(title="Legend", title_fontsize="13", fontsize="12")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

# Save and show the plot
plt.savefig("EU_Gas_Balance_Chart.png", dpi=300)
plt.show()
{% endhighlight %}

# Global Oil Balance Column Codes
Here is the list of unique IDs which correspond to different columns of data in our global oil balance. The code:

<div style="font-size: 8px;">
{% seo %} {% include head-custom.html %}
{% highlight json %}
{
    "OECD_CONS": "OECD Consumption (mb/d)",
    "USA_CONS": "United States Consumption (mb/d)",
    "JPN_CONS": "Japan Consumption (mb/d)",
    "CAN_CONS": "Canada Consumption (mb/d)",
    "EUR_CONS": "Europe Consumption (mb/d)",
    "OTH_OECD_CONS": "Other OECD Consumption (mb/d)",
    "NONOECD_CONS": "Non-OECD Consumption (mb/d)",
    "CHN_CONS": "China Consumption (mb/d)",
    "IND_CONS": "India Consumption (mb/d)",
    "BRA_CONS": "Brazil Consumption (mb/d)",
    "RUS_CONS": "Russia Consumption (mb/d)",
    "OTH_NONOECD_CONS": "Other Non-OECD Consumption (mb/d)",
    "TOT_CONS": "Total World Consumption",
    "OECD_SUPP": "OECD Supply (mb/d)",
    "USA_TL_SUPP": "U.S. Total Liquids Supply (mb/d)",
    "USA_CR_SUPP": "Crude Supply (mb/d)",
    "USA_LOW48_CR_SUPP": "Lower 48 Supply (mb/d)",
    "USA_GOM_CR_SUPP": "GOM Supply (mb/d)",
    "USA_AL_CR_SUPP": "Alaska Supply (mb/d)",
    "USA_NGL_SUPP": "NGLs Supply (mb/d)",
    "USA_OL_SUPP": "Other US Liquids Supply (mb/d)",
    "MEX_SUPP": "Mexico Supply (mb/d)",
    "CAN_SUPP": "Canada Supply (mb/d)",
    "OTH_OECD_SUPP": "Other OECD Supply (mb/d)",
    "NONOECD_SUPP": "Non-OECD Supply (mb/d)",
    "BRA_SUPP": "Brazil Supply (mb/d)",
    "CHN_SUPP": "China Supply (mb/d)",
    "RUS_SUPP": "Russia Supply (mb/d)",
    "RUS_CR_SUPP": "Russia Crude Supply (mb/d)",
    "OTH_NONOECD_SUPP": "Other Non-OECD Supply (mb/d)",
    "NONOPEC_SUPP": "Non-OPEC Supply (mb/d)",
    "OPEC_SUPP": "OPEC Supply (mb/d)",
    "OPEC_CR_SUPP": "Crude Oil Portion Supply (mb/d)",
    "OPEC_OL_SUPP": "Other Liquids Supply (mb/d)",
    "GLOBAL_BIOFUELS_SUPP": "Global Biofuels Supply",
    "GLOBAL_PROC_GAINS": "Global Processing Gains",
    "TOT_SUPP": "Total World Supply (mb/d)",
    "SURPLUS": "Implied Surplus (mb/d)",
    "OECD_IND_STK_CHNG": "OECD Industry Stock Change (mb/d)",
    "USA_IND_STK_CHNG": "US Industry Stocks Change (Ex. SPR) (mb/d)",
    "OTH_OECD_IND_STK_CHNG": "Other OECD Industry Stocks Change (mb/d)",
    "OTH_STK_CHNG": "Other Stock Change* (mb/d)",
    "CHN_STK_CHNG": "Chinese Crude Stocks Change (mb/d)",
    "OECD_SPR_STK_CHNG": "OECD SPR Change (mb/d)",
    "TOT_OOW_CHNG": "Oil on Water Change (mb/d)",
    "OTH_NONOECD_STK_CHNG": "Other Non-OECD Stocks Change (mb/d)",
    "OPEC_SPARECAP": "OPEC Spare Capacity (mb/d)",
    "BRENT_PRICE": "Brent Forecast ($)",
    "WTI_PRICE": "WTI Forecast ($)",
    "BRENT_WTI_SPREAD": "Brent-WTI Spread ($)"
}

{% endhighlight %}
</div>

# Conclusion
RapidanAPI is in its early stages of development, but we plan on regularly expanding the number and quality of datasets that are available. If you have any questions about RapidanAPI or need help with its implementation, don't hesitate to reach out.
