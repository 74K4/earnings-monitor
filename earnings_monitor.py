import os
import requests

API_KEY = os.environ["FMP_API_KEY"]

url = f"https://financialmodelingprep.com/stable/earnings?symbol=NVDA&apikey={API_KEY}"

data = requests.get(url).json()

latest = None

for row in data:
    if row["epsActual"] is not None:
        latest = row
        break

print("Ticker:", latest["symbol"])
print("Date:", latest["date"])
print("EPS Actual:", latest["epsActual"])
print("EPS Estimate:", latest["epsEstimated"])
