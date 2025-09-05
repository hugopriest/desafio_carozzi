# Funciones para carga y limpieza de datos

import pandas as pd
from datetime import datetime

def load_data(file_path: str, dtypes: dict, parse_dates: list = None) -> pd.DataFrame:
    if parse_dates is None:
        parse_dates = []
    df = pd.read_csv(file_path, dtype=dtypes, parse_dates=parse_dates)
    return df