import os
import requests

API_KEY = os.environ["FMP_API_KEY"]
WEBHOOK = os.environ["DISCORD_WEBHOOK"]

url = f"https://financialmodelingprep.com/stable/earnings?symbol=NVDA&apikey={API_KEY}"

data = requests.get(url).json()

latest = None

for row in data:
    if row["epsActual"] is not None:
        latest = row
        break

eps_beat = latest["epsActual"] > latest["epsEstimated"]
rev_beat = latest["revenueActual"] > latest["revenueEstimated"]

message = {
    "content":
    f"""@everyone

NVDA

Date: {latest['date']}

EPS Actual: {latest['epsActual']}
EPS Estimate: {latest['epsEstimated']}
EPS Beat: {eps_beat}

Revenue Actual: {latest['revenueActual']}
Revenue Estimate: {latest['revenueEstimated']}
Revenue Beat: {rev_beat}
"""
}

response = requests.post(
    WEBHOOK,
    json=message
)

print(response.status_code)
