import requests
import json
from config import make_url, items, get_choice_item


def get_api(url):
    response = requests.get(url)
    return json.loads(response.text)


def show_rate(url, choice_item):
    rate = get_api(url)
    rate_value = rate[items[choice_item]]['value']
    rate_date = rate[items[choice_item]]['date']
    return rate_value, rate_date 


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