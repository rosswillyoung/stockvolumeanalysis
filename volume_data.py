
import yfinance as yf
from pandas_datareader import data as pdr
import csv
from datetime import date, timedelta
import sqlite3

yf.pdr_override()
company_list = []


def get_stocks():
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


def add_stocks_to_csv():
    with open('newcompanyvolume.csv', 'w', newline='') as csvfile:
        for i in company_list:
            writer = csv.writer(csvfile, delimiter=',')
            try:
                volume = get_average_volume(str(i))
            except:
                pass
            writer.writerow([str(i), str(volume)])


def get_volume_and_price(symbol):
    data = pdr.get_data_yahoo(symbol, date.today(),
                              date.today() + timedelta(days=1))
    high = data['High']
    volume = data['Volume']
    return int(volume), float(high)


def get_days_high(symbol, date):
    data = pdr.get_data_yahoo(symbol, date, date + timedelta(days=1))
    high = data['High']
    return float(high)


def get_last_weeks_data(conn, date):
    c = conn.cursor()
    c.execute("SELECT * FROM volume_data WHERE date = ?", (date,))
    return c.fetchall()


def main():
    get_stocks()
    add_stocks_to_csv()


if __name__ == '__main__':
    main()
