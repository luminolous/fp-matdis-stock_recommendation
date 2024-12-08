import requests
import pandas as pd

url = "https://www.alphavantage.co/query?function=CASH_FLOW&symbol=IBM&apikey=demo&datatype=csv"
data = pd.read_csv(url)

print(data.head())