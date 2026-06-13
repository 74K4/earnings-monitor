import os
import requests
import json

API_KEY = os.environ["FMP_API_KEY"]
WEBHOOK = os.environ["DISCORD_WEBHOOK"]

try:
    with open("last_results.json", "r") as f:
        old_results = json.load(f)
except:
    old_results = {}

new_results = {}

stocks = [
    "NVDA",
    "META",
    "AMZN",
    "GOOGL",
    "MSFT"
]

for stock in stocks:

    print("==========")
    print(stock)

    url = f"https://financialmodelingprep.com/stable/earnings?symbol={stock}&apikey={API_KEY}"

    data = requests.get(url).json()

    latest = None

    for row in data:

        if row["epsActual"] is not None:

            latest = row

            break

    if latest is None:

        print("決算データなし")

        continue

    eps_beat = latest["epsActual"] > latest["epsEstimated"]
    rev_beat = latest["revenueActual"] > latest["revenueEstimated"]

    current_status = eps_beat and rev_beat
    
    new_results[stock] = current_status

    print("EPS Beat =", eps_beat)
    print("Revenue Beat =", rev_beat)

    old_status = old_results.get(stock)

    if old_status != current_status:
        
    message = {
        "content":
        f"""@everyone

    {stock}

    状態変化を検出

    前回: {old_status}
    今回: {current_status}

    Date: {latest['date']}
    """
    }
with open("last_results.json", "w") as f:
    json.dump(
        new_results,
        f,
        indent=4
    )
    
EPS Actual: {latest['epsActual']}
EPS Estimate: {latest['epsEstimated']}

Revenue Actual: {latest['revenueActual']}
Revenue Estimate: {latest['revenueEstimated']}

EPS Beat: True
Revenue Beat: True
"""
        }

        response = requests.post(
            WEBHOOK,
            json=message
        )

        print(f"{stock} 通知送信")
