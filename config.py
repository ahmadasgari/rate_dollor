# date_desired = input("Please insert date desired( for example : 1398-02-15):")
from data import url


items = {"1": "sekkeh", "2": "usd_buy", "3": "usd_sell"}


def get_choice_item():
    choice_items = input(
        "for rate gold coin(sekkeh) number 1 \n"
        "for rate dollor_buy(USD) number 2\n"
        "for rate dollor_sell(USD) number 3\n"
        "Please insert date desired (1 or 2 or 3) : ").strip()

    if choice_items not in ('1', '2', '3'):
        return get_choice_item()

    return choice_items


def make_url(item):
    return f'{url}&item={item}'


