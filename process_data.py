import sqlite3
from datetime import date


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


# print(add_stock_to_table('MSFT', 100000, 100000))

# conn = sqlite3.connect('stocks.db')

# c = conn.cursor()
# c.execute("SELECT * FROM volume_data")
# print(c.fetchall())

# conn.commit()
# conn.close()

def update_price(symbol, price, date):
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    c.execute("UPDATE volume_data SET price_at_close = ? WHERE symbol = ? AND date = ?", (price, symbol, date))

update_price('MSFT', 20.0, '')
