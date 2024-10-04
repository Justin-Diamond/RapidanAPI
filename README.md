![Anniversary Banner](https://github.com/user-attachments/assets/d194dd94-c2b9-4def-82fc-233f81796aa5)
# RapidanAPI: Insights made convenient.

Welcome to RapidanAPI! This Python Package helps Rapidan's clients process API-accessible data and forecasts as conveniently as possible.

RapidanAPI is currently in Version 1.1.2, but we’re already working to expand the number and extensiveness of datasets available through RapidanAPI. If you have any questions about RapidanAPI or need help with its implementation, don't hesitate to reach out.

# Getting started with RapidanAPI
The easiest way to install this package is to use the package installer for Python, which enables a "pip" command. The tutorial for using the package installer can be found here: https://packaging.python.org/en/latest/tutorials/installing-packages/

The RapidanAPI package can be installed with the command "pip install RapidanAPI" either on your own computer or in a virtual environment. Installation should only take a few seconds!

# Available Endpoints
Once this package is installed, you can access most datasets with a few lines of code and an API key – but endpoints like the Global Oil Balance have some extra parameters. Here is a list of endpoints and their parameters:

{% seo %} {% include head-custom.html %}
{% highlight html %}
Endpoint : Parameters

global_oil_balance : api_key, balance_date, columns
refined_products_outlook : api_key
barrels_at_risk : api_key
china_risk_tracker : api_key
energy_calendar : api_key
us_gas_balance : api_key
eu_gas_balance : api_key
{% endhighlight %}

# API Keys
The "api_key" parameter contains your api key, which is used to identify you as a legitimate user and should be kept secret. The default usage plan allows each key to make up to 30000 requests per month. You can reach out to Rapidan at any time to inquire about API key access. Endpoints which only require the API key parameter will always pulls the most current & complete version of the dataset. Here's how you can pull energy calendar data using only the “api_key” parameter:

{% seo %} {% include head-custom.html %}
{% highlight python %}
from RapidanAPI import energy_calendar

# API key is passed as a parameter
api_key = "YOUR_API_KEY"

# Get the data
df = energy_calendar(api_key)

# df is a pandas DataFrame containing the calendar
print(df)

# Output a csv file
df.to_csv("Energy_Calendar.csv")
{% endhighlight %}

This outputs a table that can be saved as a .csv, .xlsx, or other file:

{% seo %} {% include head-custom.html %}
{% highlight html %}
  Stars     Date/Event                                        Description
0    **  Month of July  Trinidad and Tobago’s Atlantic LNG (ALNG) Trai...
1    **  Month of July  Russia’s Sakhalin II LNG undergoes scheduled m...
2    **  Month of July  Final FERC Commissioner likely to be sworn in....
3    *	 July 9	        US House Financial Services Cmte hearing: Annu...
4    *** July 10        OPEC releases its July Monthly Oil Market Rep....
{% endhighlight %}

# Other Parameters
For datasets like the Global Oil Balance, parameters such as “balance_date” and “columns” are included to give you extra control of the data, and allow you to retrieve historical oil balances. In the future, we plan on adding these parameters to other endpoints – such as the refined products outlook and gas balance endpoints.

The “balance_date” parameter is in YYMM format, and includes our historical oil balances from 2401 (January 2024) to present. For example, setting the date parameter as 2401 will pull data from January 2024, and setting it as 2407 will pull data from July 2024. If you want to pull the most recently updated dataset, just set this parameter as balance_date="Current" or balance_date=None.

The “columns” parameter lets you pull specific columns of data. If you want to pull the entire dataset, just set this parameter as columns="All" or columns=None. But if you want to pull specific columns, just enter one or more of the column codes listed at the bottom of this page as comma separated values. For example, columns=“OECD_CONS, OECD_SUPP” will pull OECD consumption and OECD supply. Here’s how you can pull all of the columns from our June 2023 global oil balance:

{% seo %} {% include head-custom.html %}
{% highlight python %}
from RapidanAPI import global_oil_balance

# API key, balance ID, and columns are passed as parameters
api_key = "YOUR_API_KEY"
balance_id = "2408"
columns = "All"

# Get the data
df = global_oil_balance(api_key, balance_id, columns)

# df is a pandas DataFrame containing the data
print(df)

# Output a csv file
df.to_csv("Global_Oil_Balance.csv")
{% endhighlight %}

Which outputs a dataframe & .csv that looks like this:

{% seo %} {% include head-custom.html %}
{% highlight html %}
   Quarter (2408)  OECD Consumption (mb/d)  ...  WTI Forecast ($)  Brent-WTI Spread ($)
0            1Q23                     45.3  ...              76.1                   6.0
1            2Q23                     45.8  ...              73.6                   4.2
2            3Q23                     46.2  ...              82.1                   3.8
3            4Q23                     46.3  ...              78.4                   4.4
4            1Q24                     45.1  ...              76.9                   4.9
5            2Q24                     46.1  ...              80.6                   4.4
6            3Q24                     46.5  ...              77.3                   3.5
7            4Q24                     46.6  ...              79.3                   4.0
8            1Q25                     45.8  ...              80.7                   4.0
9            2Q25                     45.9  ...              80.1                   4.0
10           3Q25                     46.7  ...              77.7                   4.0
11           4Q25                     47.0  ...              75.5                   4.0
{% endhighlight %}

# More Example Code
For your convenience, this section contains a few chunks of example code.

Here's a script that pulls and prints every dataframe available through RapidanAPI:

{% seo %} {% include head-custom.html %}
{% highlight python %}
from RapidanAPI import global_oil_balance, china_risk_tracker, refined_products_outlook, barrels_at_risk, eu_gas_balance, us_gas_balance, energy_calendar
import pandas as pd

api_key = "YOUR_API_KEY"

# Pull data from each endpoint and store in a DataFrame
global_oil_balance_df = global_oil_balance(api_key, balance_date="Current", columns="All")
refined_products_df = refined_products_outlook(api_key)
barrels_at_risk_df = barrels_at_risk(api_key)
china_risk_tracker_df = china_risk_tracker(api_key)
eu_gas_balance_df = eu_gas_balance(api_key)
us_gas_balance_df = us_gas_balance(api_key)
energy_calendar_df = energy_calendar(api_key)

# Print each DataFrame with combined text
print("Global Oil Balance DataFrame:\n", global_oil_balance_df.head(), "\n")
print("Refined Products Outlook DataFrame:\n", refined_products_df.head(), "\n")
print("Barrels at Risk DataFrame:\n", barrels_at_risk_df.head(), "\n")
print("China Risk Tracker DataFrame:\n", china_risk_tracker_df.head(), "\n")
print("EU Gas Balance DataFrame:\n", eu_gas_balance_df.head(), "\n")
print("US Gas Balance DataFrame:\n", us_gas_balance_df.head(), "\n")
print("Energy Calendar DataFrame:\n", energy_calendar_df.head(), "\n")
{% endhighlight %}

The following script uses the "openpyxl" package (which can be installed with the command "pip install openpyxl") to write all of the endpoints to an excel file called "Rapidan_Data.xlsx."

{% seo %} {% include head-custom.html %}
{% highlight python %}
from RapidanAPI import (global_oil_balance, china_risk_tracker, refined_products_outlook, barrels_at_risk, eu_gas_balance, us_gas_balance, energy_calendar)
import pandas as pd

api_key = "YOUR_API_KEY"

with pd.ExcelWriter("Rapidan_Data.xlsx", engine="openpyxl") as writer:
    global_oil_balance(api_key, balance_date="Current", columns="All").to_excel(writer, sheet_name="Global_Oil_Balance", index=False)
    refined_products_outlook(api_key).to_excel(writer, sheet_name="Refined_Products", index=False)
    barrels_at_risk(api_key).to_excel(writer, sheet_name="Barrels_at_Risk", index=False)
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

# Pull df from the EU gas balance and process date column
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

This outputs the following chart as a .png file:
![Rapidan_EU_Gas_Balance](https://github.com/user-attachments/assets/5045e14d-cde9-41d8-a5e1-7ab27d549f64)

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
