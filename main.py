import requests
import json
from config import make_url, items, get_choice_item


def get_api(address):
    response = requests.get(address)
    return json.loads(response.text)


def show_rate(address, choice_item):
    rate = get_api(address)
    return rate[items[choice_item]]['value'], rate[items[choice_item]]['date']


def run():
    choice_item = get_choice_item()
    url = make_url(items[choice_item])
    final_rate = show_rate(url, choice_item)

    print('*' * 30)
    print(f'item : {items[choice_item]}')
    print(f'ِDate and time : {final_rate[1]}')
    print(f'final rate : {final_rate[0]}')

    play_again = input('if you want try again please press (y)'
                       ' and for exit press (q): ')

    if play_again == 'y':
        return run()

    print('see you')


if __name__ == '__main__':
    run()