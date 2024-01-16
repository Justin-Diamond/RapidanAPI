# RapidanAPI allows Rapidan's clients to conveniently pull energy data.

The RapidanAPI module and its dependencies can be installed with "pip install RapidanAPI".

Once this package is installed, various Rapidan datasets can be accessed with just a few lines of code and an API key. By changing the "endpoints" and "parameters", you can modify which dataset and columns of data will be pulled by your python script.

{% seo %} {% include head-custom.html %}
{% highlight python %}
from RapidanAPI import global_oil_balance

# The API key, balance ID, and columns to return
api_key = "RAPIDAN_API_KEY"
balance_id = "2311"
columns = "Balance"

# Get the data
df = global_oil_balance(api_key, balance_id, columns)

# Now df is a pandas DataFrame containing the data
print(df)

# Output a csv file
df.to_csv("output.csv")
{% endhighlight %}

Endpoints will each have 3 parameters: an api_key, an id, and a columns parameter.

The "api_key" parameter will contain your api_key, which can be set as a secret variable.

The "id" parameter will differ based on the endpoint being used. The id parameter will always be named by appending the last part of the endpoint's name to "id" with an underscore. For example, the id parameter for the "global_oil_balance" endpoint is "balance_id", and for the "energy_calendar is "calendar_id". If no ID is passed through, then the most up-to-date version of the endpoint will be pulled.

The "columns" parameter will pull the entire dataset as long as the last part of the endpoint's name is written. For example, writing "Balance" in this parameter will pull the entire balance. If you wish to pull only specific columns, then refer to the dictionary called "uniqueIDs.json" on our GitHub page, and input unique identifiers in the columns parameter, separated by commas, to pull only the columns of data you desire.

Each user is currently limited to 1500 API calls per month. However, the rate limit can be reset or modified upon request. Please reach out to Rapidan Energy Group for access to an API key.
