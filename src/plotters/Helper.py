from typing import Iterable, Union, List
from datetime import datetime
import numpy as np


class Helper:
    @staticmethod
    def get_simple_bin_xticks(x: Iterable[int], last_bin_inf: bool = False) -> List[str]:
        xticks = [str(_x) for _x in x]
        if last_bin_inf:
            xticks[-1] = f">={xticks[-1]}"
        
        return xticks
    
    weekdays_xticks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    @staticmethod
    def get_range_bin_xticks(x: Iterable[Union[int, float]]) -> List[str]:
        xticks = [f'[{x_start:.0f}, {x_end:.0f})' for x_start, x_end in zip(x[:-1], x[1:])]
        xticks[-1] = f'{xticks[-1][:-1]}]'
        return xticks
    
    @staticmethod
    def get_breaks_xticks():
        borders = ['0s', '1s', '5s', '10s', '30s', '1m', '2m', '3m', '5m', '10m', '30m', '1h', '24h']
        xticks = [f'[{a}, {b})' for a, b in zip(borders[:-1], borders[1:])]
        xticks[-1] = f'{xticks[-1][:-1]}]'
        return xticks

    @staticmethod
    def get_date_xticks(date_range: np.ndarray):
        date_list = [datetime.fromisoformat(str(date)) for date in date_range]
        return [date.strftime('%b %d') for date in date_list]
