import argparse
from enum import Enum


class Currency(Enum):
    EUR = 'EUR'
    USD = 'USD'

    def __str__(self):
        return self.value


class DeGiroPitConfig:
    date_column_name_default = "Datum"
    currency_default = Currency.EUR

    def __init__(self, args) -> None:
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--date_column_name",
                            help=f"Name of date column in the CSV file. Default is {DeGiroPitConfig.date_column_name_default}.",
                            default=DeGiroPitConfig.date_column_name_default)
        parser.add_argument("--currency", type=Currency, choices=list(Currency), default=DeGiroPitConfig.currency_default)
        args = parser.parse_args(args)
        self.date_column_name = args.date_column_name
        self.currency = args.currency
