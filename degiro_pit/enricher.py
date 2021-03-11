import pandas as pd

from degiro_pit.config import DeGiroPitConfig
from degiro_pit.nbp_api import NbpApi


def enrich(args):
    config = DeGiroPitConfig(args)
    nbp_api = NbpApi()
    transactions = pd.read_csv("../data/Transactions.csv")
    transactions["pd_date"] = pd.to_datetime(transactions[config.date_column_name])
    transactions["previous_workday"] = transactions["pd_date"] - pd.tseries.offsets.BDay(1)
    transactions[f"{config.currency}_PLN_day_before"] = \
        transactions["previous_workday"].dt.strftime('%Y-%m-%d').apply(lambda date: nbp_api.get_pln(date, config.currency))
    transactions.to_csv("../data/output.csv")


def _main():
    import sys
    enrich(sys.argv[1:])


if __name__ == "__main__":
    _main()
