# date_desired = input("Please insert date desired( for example : 1398-02-15):")
from data import url


items = {"1": "sekkeh", "2": "usd_buy"}


def get_choice_item():
    choice_item = input(
        "for rate gold coin(sekkeh) number 1 \n"
        "for rate dollor(USD) number 2\n"
        "Please insert date desired (1 or 2 ) : ").strip()

    if choice_item not in ('1', '2'):
        return get_choice_item()

    return choice_item


def make_url(item):
    print(f'{url}&item={item}')
    return f'{url}&item={item}'


make_url(items[get_choice_item()])
