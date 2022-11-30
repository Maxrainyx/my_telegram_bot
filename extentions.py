import requests
import json
from config import keys, header


class Converter:
    @staticmethod
    def get_price(to_cur: str, from_cur: str, amount: str):
        if to_cur == from_cur:
            raise ConversionException(f'Невозможно перевести одинаковые валюты "{from_cur}".')
        try:
            to_cur_ticker = keys[to_cur]
        except KeyError:
            raise ConversionException(f'Hе удалось обработать валюту "{to_cur}"')
        try:
            from_cur_ticker = keys[from_cur]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту "{from_cur}"')
        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количество "{amount}"')
        url = f"https://api.apilayer.com/fixer/convert?to={to_cur_ticker}&from={from_cur_ticker}&amount={amount}"
        r = requests.get(url, header)
        result = json.loads(r.content)['result']
        return result


class ConversionException(Exception):
    pass

