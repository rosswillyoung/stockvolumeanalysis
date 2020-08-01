import csv
import requests
import json
import time

with open('companyvolume.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        symbol = row[0]
        average_volume = row[1]


def compare_volume_to_average(symbol, average_volume):
    r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" +
                     symbol + "&interval=60min&apikey=CAEGOUULJ7SV7EVB")

    json_output = json.loads(r.text)['Time Series (60min)']

    return
