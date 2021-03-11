from urllib.request import urlopen
import json

from degiro_pit.config import Currency


class NbpApi:

    @staticmethod
    def get_pln(date, currency: Currency):
        url = f"http://api.nbp.pl/api/exchangerates/rates/A/{currency}/{date}/?format=json"
        res = json.loads(urlopen(url).read().decode("utf-8"))
        return res["rates"][0]["mid"]

