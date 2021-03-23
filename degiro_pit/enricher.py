import pandas as pd

from degiro_pit.date_tax import DateTaxPoland
from degiro_pit.config import DeGiroPitConfig
from degiro_pit.nbp_api import NbpApi


def enrich(args):
    config = DeGiroPitConfig(args)
    nbp_api = NbpApi()
    transactions = pd.read_csv("../data/Transactions.csv")
    transactions["pd_date"] = pd.to_datetime(transactions[config.date_column_name], dayfirst=True)
    date_tax = DateTaxPoland()
    transactions["previous_workday"] = date_tax.get_tax_date(transactions["pd_date"])
    transactions[f"{config.currency}_PLN_day_before"] = \
        transactions["previous_workday"].dt.strftime('%Y-%m-%d').apply(lambda date: get_currency_pln(date, nbp_api, config.currency))
    transactions.to_csv("../data/output.csv")


def get_currency_pln(date, nbp_api, currency):
    res = nbp_api.get_pln(date, currency)
    if res is None:
        print(f"Can't get currency value for the date {date}. Please raise an issue in the project on Github.")
    return res


def _main():
    import sys
    enrich(sys.argv[1:])


if __name__ == "__main__":
    _main()
