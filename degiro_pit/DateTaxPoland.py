import holidays
from pandas import Series
from pandas.tseries import offsets


class DateTaxPoland:
    """
    Class for calculations of Tax date from transaction date.
    In Poland it's a workday before the transaction.
    """

    def __init__(self) -> None:
        self.holidays_calendar = holidays.PL()

    def get_tax_date(self, transactions_date: Series) -> Series:
        """

        :param transactions_date: pandas column of dates
        :return: pandas column of tax dates
        """
        workday_candidate = transactions_date - offsets.BDay(1)
        self._move_back_if_holidays(workday_candidate)
        return workday_candidate

    def _move_back_if_holidays(self, workday_candidate):
        check_holidays = True
        while check_holidays:
            is_holiday = [x in self.holidays_calendar for x in workday_candidate]
            workday_candidate[is_holiday] -= offsets.BDay(1)
            check_holidays = sum(is_holiday) > 0
