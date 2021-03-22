import json
from typing import Union
from urllib.error import HTTPError
from urllib.request import urlopen

from degiro_pit.config import Currency


class NbpApi:

    @staticmethod
    def get_pln(date, currency: Currency) -> Union[float, None]:
        """
        Call NBP API to get currency/PLN value for date.

        :param date: date in format YYYY-MM-DD
        :param currency: currency enum
        :return: currency/PLN value. None when there is no value for date, e.g. holidays.
        """
        url = f"http://api.nbp.pl/api/exchangerates/rates/A/{currency}/{date}/?format=json"
        try:
            res = json.loads(urlopen(url).read().decode("utf-8"))
            return res["rates"][0]["mid"]
        except HTTPError as err:
            if err.code == 404:
                return None
            else:
                raise err
