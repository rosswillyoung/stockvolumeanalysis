import sqlite3
from datetime import date

import volume_data


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


def main():
    database = r'C:\Users\Ross\Documents\pythonfun\stockvolume\stocks.db'

    # conn = create_connection(database)
    # with conn:
    #     update_price_and_volume(conn, (9999, 78877000, 'MSFT', '2020-08-03'))

    volume, high = volume_data.get_volume_and_price('fb')
    print(volume)
    print(high)


if __name__ == '__main__':
    main()
