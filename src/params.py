# Parámetros para la carga de datos
import pandas as pd
import holidays

class Params:
    def __init__(self):
        self.DATA_PATH = '../src/data/data.csv'
        self.DATA_DATASET = {
            'id': 'object', 
            'date': 'datetime64[ns]', 
            'store_nbr': 'object', 
            'family': 'object', 
            'sales': 'float64', 
            'onpromotion': 'int64'
        }
        self.STORES_PATH = '../src/data/stores.csv'
        self.STORES_DATASET = {
            'store_nbr': 'object',
            'city': 'object',
            'state': 'object',
            'type': 'object',
            'cluster': 'int64'
        }
        self.OIL_PATH = '../src/data/oil.csv'

    def get_holidays(self, init_year: int, end_year: int) -> pd.DataFrame:
        """
        Gets holidays in Ecuador for the specified range of years.
        """
        years = range(init_year, end_year + 1)
        ec_holidays = holidays.Ecuador(years=years)
        ecuador_holidays = pd.DataFrame([
            {"holiday": name, "ds": pd.to_datetime(date), "lower_window": 0, "upper_window": 1}
            for date, name in ec_holidays.items()
        ])
        return ecuador_holidays