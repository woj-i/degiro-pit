import argparse

import pandas as pd

from nbp_api import NbpApi

parser = argparse.ArgumentParser()
date_column_name_default = "Datum"
parser.add_argument("-d", "--date_column_name",
                    help=f"Name of date column in the CSV file. Default is {date_column_name_default}.",
                    default=date_column_name_default)
args = parser.parse_args()

nbp_api = NbpApi()
transactions = pd.read_csv("../data/Transactions.csv")
transactions["pd_date"] = pd.to_datetime(transactions[args.date_column_name])
transactions["previous_workday"] = transactions["pd_date"] - pd.tseries.offsets.BDay(1)
transactions["eur_pln_day_before"] = transactions["previous_workday"].dt.strftime('%Y-%m-%d').apply(lambda date: nbp_api.get_eur(date))
transactions.to_csv("../data/output.csv")
