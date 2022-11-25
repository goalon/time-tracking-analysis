from collections import defaultdict
import numpy as np
from datetime import datetime


class DataGathered():
    def __init__(self):
        self.data = defaultdict(dict)
        self.data_per_day = 0

    def add(self):
        self.data_per_day += 1

    def finalize_day(self, author: str, date: datetime):
        self.data[author][date] = self.data_per_day
        self.data_per_day = 0

    @property
    def data_gathered(self):
        date_range = np.arange('2022-10-10', '2022-11-26', dtype='datetime64[D]')
        full_data = []
        for d in self.data.values():
            full_data_one = []
            for date in date_range:
                dt = datetime.fromisoformat(str(date))
                full_data_one.append(d[dt] if dt in d else 0)
            full_data.append(full_data_one)
            full_data_one = []

        return date_range, full_data
