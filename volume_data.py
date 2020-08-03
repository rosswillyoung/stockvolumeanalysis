
import yfinance as yf
from pandas_datareader import data as pdr
import csv

yf.pdr_override()
company_list = []
with open('companylist.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        company_list.append(row[0])
company_list.pop(0)


def get_average_volume(symbol):
    data = pdr.get_data_yahoo(symbol, start='2020-05-02', end='2020-08-02')
    volume_data = data['Volume']

    sum_of_items = 0
    number_of_items = 0
    for i in volume_data:
        number_of_items += 1
        sum_of_items += i

    try:
        average_volume = sum_of_items / number_of_items
    except ZeroDivisionError:
        return None

    return average_volume


with open('newcompanyvolume.csv', 'w', newline='') as csvfile:
    for i in company_list:
        writer = csv.writer(csvfile, delimiter=',')
        try:
            volume = get_average_volume(str(i))
        except:
            pass
        writer.writerow([str(i), str(volume)])
