import sqlite3
from datetime import date, timedelta

import volume_data
import send_email


def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return conn


def add_stock_to_table(symbol, current_volume, average_volume):
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    today = date.today()
    price_at_close = 0
    c.execute("""
                INSERT INTO volume_data VALUES (?, ?, ?, ?, ?)
    """, (today, symbol, current_volume, average_volume, price_at_close))
    conn.commit()
    conn.close()

    return symbol + ' added into table'


def update_price_and_volume(conn, task):
    c = conn.cursor()
    sql = "UPDATE volume_data SET price_at_close = ?, current_volume = ? WHERE symbol = ? AND date = ?"
    c.execute(sql, task)
    conn.commit()


def update_all_yesterday(conn):
    yesterday = date.today() - timedelta(days=1)
    yesterday = str(yesterday)
    # with conn:
    c = conn.cursor()
    c.execute("SELECT symbol FROM volume_data WHERE date = ?", (yesterday,))
    symbol_list = []
    for i in c.fetchall():
        symbol_list.append(i)
    # print(symbol_list)
    for i in symbol_list:
        try:
            volume, high = volume_data.get_volume_and_price(i)
            update_price_and_volume(conn, (high, volume, i[0], yesterday))
        except TypeError:
            pass


def main():
    database = r'stocks.db'
    conn = create_connection(database)
    with conn:
        update_all_yesterday(conn)
        last_week = date.today() - timedelta(days=7)
        last_weeks_data = volume_data.get_last_weeks_data(conn, last_week)
        print(last_weeks_data[0][1])
        for i in last_weeks_data:
            symbol = i[1]
            last_week_high = volume_data.get_days_high(symbol, last_week)
            todays_high = volume_data.get_days_high(symbol,
                                                    date.today())
            if last_week_high < todays_high:
                send_email.send_email(symbol + " alert")
                # print(volume_data.get_days_high('fb', day))
            else:
                print(str(last_week_high) +
                      " is greater than or equal to " + str(todays_high))


if __name__ == '__main__':
    main()
