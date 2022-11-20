from typing import List, Optional
import numpy as np
from TimeTrackingEvent import TimeTrackingEvent, TimeTrackingEventFoundation
from .Helper import Helper


class _DelToAddData():
    def __init__(self, event: Optional[TimeTrackingEventFoundation] = None):
        self.additions = event.additions if event else 0
        self.deletions = event.deletions if event else 0

    def add(self, event: TimeTrackingEvent):
        self.additions = event.additions
        self.deletions = event.deletions

    @property
    def ratio(self):
        return self.deletions / self.additions if self.additions > 0 else np.inf


class DelToAdd():
    def __init__(self):
        self.data_per_datapoint: List[_DelToAddData] = []
        self.python_data_per_datapoint: List[_DelToAddData] = []
        self.js_data_per_datapoint: List[_DelToAddData] = []
        self.data_per_single_day = _DelToAddData()
        self.data_per_day: List[_DelToAddData] = []
        self.data_per_hour = [_DelToAddData() for _ in range(24)]

    def add(self, event: TimeTrackingEvent):
        self.data_per_datapoint.append(_DelToAddData(event))
        if event.contains_python:
            self.python_data_per_datapoint.append(_DelToAddData(event.python_data))
        if event.contains_js:
            self.js_data_per_datapoint.append(_DelToAddData(event.js_data))
        self.data_per_single_day.add(event)
        self.data_per_hour[event.start.hour].add(event)

    def finalize_day(self):
        self.data_per_day.append(self.data_per_single_day)
        self.data_per_single_day = _DelToAddData()

    def _get_histogram(self, data: List[_DelToAddData]):
        ratios = [d.ratio for d in data]
        histogram = np.histogram(ratios, Helper.del_to_add_bins)[0]

        return histogram / histogram.sum()

    @property
    def del_to_add_per_datapoint(self):
        return self._get_histogram(self.data_per_datapoint)

    @property
    def python_del_to_add_per_datapoint(self):
        return self._get_histogram(self.python_data_per_datapoint)

    @property
    def js_del_to_add_per_datapoint(self):
        return self._get_histogram(self.js_data_per_datapoint)

    @property
    def del_to_add_per_day(self):
        return self._get_histogram(self.data_per_day)
