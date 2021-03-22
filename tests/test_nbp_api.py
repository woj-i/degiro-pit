from unittest import TestCase

from degiro_pit.config import Currency
from degiro_pit.nbp_api import NbpApi


class TestNbpApi(TestCase):
    test_date = "2021-01-22"

    def test_get_eur_pln(self):
        nbp = NbpApi()
        res = nbp.get_pln(TestNbpApi.test_date, Currency.EUR)
        self.assertEqual(4.5354, res)

    def test_get_usd_pln(self):
        nbp = NbpApi()
        res = nbp.get_pln(TestNbpApi.test_date, Currency.USD)
        self.assertEqual(3.7255, res)

    def test_all_currencies_are_supported(self):
        nbp = NbpApi()
        for currency in Currency:
            res = nbp.get_pln(TestNbpApi.test_date, currency)
            self.assertIsInstance(res, float)

    def test_get_none_for_holiday_date(self):
        nbp = NbpApi()
        res = nbp.get_pln("2020-11-11", Currency.EUR)
        self.assertIsNone(res)
