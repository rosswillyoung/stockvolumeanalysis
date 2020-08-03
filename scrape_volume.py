import requests
from bs4 import BeautifulSoup as bs
import re


def get_todays_volume(symbol):
    r = requests.get('https://finance.yahoo.com/quote/' + symbol)
    soup = bs(r.text, 'html.parser')
    try:
        volume = soup.find('td', {'data-test': 'TD_VOLUME-value'}).text.strip()
    except AttributeError:
        return
    try:
        return float(volume.replace(',', ''))
    except ValueError:
        return
