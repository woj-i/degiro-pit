import datetime
from unittest import TestCase

import pandas as pd

from degiro_pit.DateTaxPoland import DateTaxPoland


class TestDateTaxPoland(TestCase):
    def test_get_tax_day(self):
        test_date = "12-11-2020"
        test_frame = pd.DataFrame({'transaction_date': [test_date]})
        test_frame["test_date"] = pd.to_datetime(test_frame["transaction_date"], dayfirst=True)
        date_tax = DateTaxPoland()
        res = date_tax.get_tax_date(test_frame["test_date"])
        self.assertEqual(datetime.date(2020, 11, 10), res[0])
