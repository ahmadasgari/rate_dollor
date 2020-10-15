import requests
import json
from config import make_url, items, item_desired


def get_api():
    url = make_url()
    response = requests.get(url)
    return json.loads(response.text)


def show_rate():
    rate = get_api()
    return rate[items[item_desired]]['value'], rate[items[item_desired]]['date']


if __name__ == '__main__':
    final_rate = show_rate()
    print('*' * 30)
    print(f'item : {items[item_desired]}')
    print(f'ِDate and time : {final_rate[1]}')
    print(f'final rate : {final_rate[0]}')
