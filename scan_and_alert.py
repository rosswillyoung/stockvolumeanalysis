import csv
import json
import time
import requests

import send_email

company_volume_dict = {}
with open('companyvolume.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        company_volume_dict[row[0]] = row[1]


def compare_volume_to_average(symbol, average_volume):
    r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" +
                     symbol + "&interval=60min&apikey=CAEGOUULJ7SV7EVB")

    json_output = json.loads(r.text)['Time Series (60min)']

    for key, value in json_output.items():
        current_volume = int(value['5. volume'])
        break

    if current_volume >= (5 * average_volume):
        send_email.send_email(symbol + " alert. Average Volume: " +
                              str(average_volume) + ", volume now: " + str(current_volume))
    return symbol, current_volume, average_volume


# print(company_volume_dict)
# print(compare_volume_to_average('FB', 10))
for key, value in company_volume_dict.items():
    print(compare_volume_to_average(key, float(value)))
    time.sleep(15)

# compare_volume_to_average('FB', 10)
