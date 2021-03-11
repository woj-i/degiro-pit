from unittest import TestCase

from degiro_pit.config import DeGiroPitConfig


class TestDeGiroPitConfig(TestCase):
    def test_default_config(self):
        config = DeGiroPitConfig([])
        self.assertEqual(config.date_column_name, config.date_column_name_default)
        self.assertEqual(config.currency, config.currency_default)

    def test_filled_config(self):
        datum = "xyz"
        currency_usd = "USD"
        config = DeGiroPitConfig(["-d", datum, "--currency", currency_usd])
        self.assertEqual(config.date_column_name, datum)
        self.assertEqual(config.currency.value, currency_usd)