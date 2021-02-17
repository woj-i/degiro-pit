from urllib.request import urlopen
import json


class NbpApi:

    @staticmethod
    def get_eur(date):
        url = f"http://api.nbp.pl/api/exchangerates/rates/A/EUR/{date}/?format=json"
        res = json.loads(urlopen(url).read().decode("utf-8"))
        return res["rates"][0]["mid"]

