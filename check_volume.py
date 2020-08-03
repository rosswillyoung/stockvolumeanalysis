import csv
import requests
import json
import time

import scrape_volume
import send_email

volume_dict = {}

with open('newcompanyvolume.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        symbol = row[0]
        average_volume = row[1]
        volume_dict[symbol] = average_volume


def compare_volume_to_average(symbol, average_volume):
    current_volume = scrape_volume.get_todays_volume(symbol)
    print('Comparing ' + symbol + ' average: ' +
          average_volume + ' to current: ' + str(current_volume))

    try:
        if current_volume > (5 * float(average_volume)):
            # print(symbol + 'average volume: ' + average_volume +
            #   'current volume: ' + str(current_volume))
            message = ("Subject: " + symbol + "\n" +
                       symbol + "'s current volume is " +
                       str(current_volume) + ", \n"
                       + "Average volume is: " + average_volume + "\n\n\n" +
                       "https://finance.yahoo.com/quote/" + symbol
                       )
            send_email.send_email(message)
    except ValueError:
        return
    except TypeError:
        return


for key in volume_dict:
    # print(key, volume_dict[key])
    compare_volume_to_average(key, volume_dict[key])
    time.sleep(1)
