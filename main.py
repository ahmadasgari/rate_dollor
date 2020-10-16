import requests
import json
from config import make_url, get_choice_item, items


def get_api(item):
    url = make_url(items[item])
    response = requests.get(url)
    return json.loads(response.text)


def show_rate(item):
    rate = get_api(item)
    return rate[items[item]]['value'], rate[items[item]]['date']


if __name__ == '__main__':
    choice_items = get_choice_item()
    final_rate = show_rate(choice_items)
    print('*' * 30)
    print(f'item : {items[choice_items]}')
    print(f'ِDate and time : {final_rate[1]}')
    print(f'final rate : {final_rate[0]}')
