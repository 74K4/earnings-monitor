import os
import requests

API_KEY = os.environ["FMP_API_KEY"]

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

    print("Date:", latest["date"])
    print("EPS Beat:", eps_beat)
    print("Revenue Beat:", rev_beat)
