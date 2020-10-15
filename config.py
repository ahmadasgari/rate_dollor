# date_desired = input("Please insert date desired( for example : 1398-02-15): ")
items = {"1": "sekkeh", "2": "usd_buy"}
item_desired = input(
    "for sekkeh number 1 \n"
    "for doller number 2\n"
    "Please insert date desired (1 or 2 ) : ")


def input_varibale(v1):
    def input_item(func):
        def wrapper(*args, **kwargs):
            a = func(*args, **kwargs)
            url2 = f"{a}&item={v1}"
            return url2

        return wrapper

    return input_item


@input_varibale(items[item_desired])
def make_url():
    KEY_API = 'cY1y8nCipbHVl0m99VSrn3bWceXbsx1a'
    url = f"http://api.navasan.tech/latest/?api_key={KEY_API}"
    return url

