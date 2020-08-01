import requests
import json
import time
import csv

company_list = []
with open('companylist.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # print(row[0])
        company_list.append(row[0])

company_list.pop(0)


def get_average_volume(symbol):
    r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" +
                     symbol + "&interval=60min&apikey=CAEGOUULJ7SV7EVB")

    try:
        json_output = json.loads(r.text)['Time Series (60min)']
    except KeyError:
        time.sleep(10)
        # get_average_volume(symbol)
        return

    sum_of_items = 0
    number_of_items = 0

    for key, value in json_output.items():
        date = key
        volume = int(value['5. volume'])
        if volume == 0:
            return
        sum_of_items += volume
        number_of_items += 1

    average_volume = sum_of_items / number_of_items
    # print('Average Volume for ' + symbol + ': ' + str(average_volume))
    return average_volume

    # print(i)
    # get_average_volume(str(i))
with open('companyvolume.csv', 'w', newline='') as csvfile:
    for i in company_list:
        writer = csv.writer(csvfile, delimiter=',')
        volume = get_average_volume(str(i))
        if volume:
            writer.writerow([str(i), str(volume)])
        time.sleep(.5)
