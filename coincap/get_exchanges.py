import csv

import requests


BEARER_TOKEN = "d2765ac92b1c5ac9f4d65fac1092830b17ebd8af4a48b7cc8cb1bf9192d3bcca"

# Read data from API
url = "https://rest.coincap.io/v3/exchanges"
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json"
}
response = requests.get(url, headers=headers)
data = response.json()["data"]

# Write data to CSV
with open("exchanges.csv", "w") as f:
    fieldnames = [
        "exchangeId",
        "name",
        "rank",
        "percentTotalVolume",
        "volumeUsd",
        "tradingPairs",
        "socket",
        "exchangeUrl",
        "updated",
    ]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for each in data:
        writer.writerow(each)