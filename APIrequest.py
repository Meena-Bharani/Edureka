import requests
import json

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data['Meta Data'])
    Time_Series_5min = data['Time Series (5min)']
    for ts in Time_Series_5min:
        time_series = Time_Series_5min[ts]
        if len(time_series)>0:
            for i in time_series:
                print(time_series[i])
