from unittest import TestCase

from nbp_api import NbpApi


class TestNbpApi(TestCase):
    def test_get_eur(self):
        nbp = NbpApi()
        res = nbp.get_eur("2021-01-22")
        self.assertEqual(res, 4.5354)
