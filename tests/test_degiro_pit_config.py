from unittest import TestCase

from degiro_pit.config import DeGiroPitConfig


class TestDeGiroPitConfig(TestCase):
    transactions_file = "Transactions.csv"

    def test_empty_config(self):
        with self.assertRaises(SystemExit):
            DeGiroPitConfig([])

    def test_default_config(self):
        config = DeGiroPitConfig([TestDeGiroPitConfig.transactions_file])
        self.assertEqual(TestDeGiroPitConfig.transactions_file, config.transactions_file)
        self.assertEqual(config.date_column_name, config.date_column_name_default)
        self.assertEqual(config.currency, config.currency_default)

    def test_filled_config(self):
        datum = "xyz"
        currency_usd = "USD"
        config = DeGiroPitConfig([TestDeGiroPitConfig.transactions_file, "-d", datum, "--currency", currency_usd])
        self.assertEqual(TestDeGiroPitConfig.transactions_file, config.transactions_file)
        self.assertEqual(config.date_column_name, datum)
        self.assertEqual(config.currency.value, currency_usd)
