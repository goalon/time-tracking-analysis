from typing import List, Optional
import numpy as np
from TimeTrackingEvent import TimeTrackingEvent


class _DelToAddData():
    def __init__(self, event: Optional[TimeTrackingEvent] = None):
        self.additions = event.additions if event else 0
        self.deletions = event.deletions if event else 0

    def add(self, event: TimeTrackingEvent):
        self.additions = event.additions
        self.deletions = event.deletions

    @property
    def ratio(self):
        return self.deletions / self.additions if self.additions > 0 else 1e9


class DelToAdd():
    def __init__(self):
        self.data_per_datapoint: List[_DelToAddData] = []
        self.data_per_single_day = _DelToAddData()
        self.data_per_day = []
        self.data_per_hour = [_DelToAddData() for _ in range(24)]

    def add(self, event: TimeTrackingEvent):
        self.data_per_datapoint.append(_DelToAddData(event))
        self.data_per_single_day.add(event)
        self.data_per_hour[event.start.hour].add(event)

    def finalize_day(self):
        self.data_per_day.append(self.data_per_single_day)
        self.data_per_single_day = _DelToAddData()

    @property
    def del_to_add_per_datapoint(self):
        ratios = [d.ratio for d in self.data_per_datapoint]
        bins = np.concatenate((np.arange(0, 3, 0.25), [np.inf]))
        histogram = np.histogram(ratios, bins)[0]

        return histogram / histogram.sum()
