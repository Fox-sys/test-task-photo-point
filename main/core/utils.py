from main.core.exceptions import InvalidApiKeyException
from django.conf import settings
import requests
import logging


def get_usd_price_in_rub():
    data = requests.get(
        f'https://api.currencyapi.com/v3/latest?apikey={settings.CURRENCY_APIKEY}&currencies=RUB').json()
    try:
        result = {"usd": 1, "rub": data['data']['RUB']['value']}
    except KeyError as e:
        logging.log(logging.WARNING, 'Check api key in .env file')
        raise InvalidApiKeyException
    return result
