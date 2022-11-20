from collections import defaultdict
from typing import List, DefaultDict, Literal
import numpy as np
from datetime import datetime
from TimeTrackingEvent import TimeTrackingEvent
from .Helper import Helper


class _ActivityPerHourData:
    def __init__(self):
        self.datapoints = 0
        self.actions = 0
    
    def add(self, event: TimeTrackingEvent):
        self.datapoints += 1
        self.actions += event.actions

    @property
    def actions_per_datapoint(self):
        return self.actions / self.datapoints if self.datapoints > 0 else 0


class ActivityPerHour:
    def __init__(self):
        hours_data_creator = lambda: [_ActivityPerHourData() for _ in range(24)]
        
        self.total_data = defaultdict(hours_data_creator)
        self.python_data = defaultdict(hours_data_creator)
        self.js_data = defaultdict(hours_data_creator)

    def add(self, event: TimeTrackingEvent):
        self.total_data[event.author][event.start.hour].add(event)
        if event.contains_python:
            self.python_data[event.author][event.start.hour].add(event)
        if event.contains_js:
            self.js_data[event.author][event.start.hour].add(event)

    def _get_data_total(self, data: DefaultDict[str, List[_ActivityPerHourData]], by: Literal['datapoints', 'actions']):
        data_by_by = [[getattr(d, by) for d in user_data] for user_data in data.values()]
        return np.asarray(data_by_by).sum(axis=0)

    def _get_data_percentage(self, data: DefaultDict[str, List[_ActivityPerHourData]], by: Literal['datapoints', 'actions']):
        total_data_by_by = self._get_data_total(data, by)
        return total_data_by_by / total_data_by_by.sum()

    @property
    def total_activity_per_hour_by_datapoints(self):
        return self._get_data_percentage(self.total_data, 'datapoints')

    @property
    def total_activity_per_hour_by_actions(self):
        return self._get_data_percentage(self.total_data, 'actions')

    @property
    def python_activity_per_hour_by_datapoints(self):
        return self._get_data_percentage(self.python_data, 'datapoints')

    @property
    def js_activity_per_hour_by_datapoints(self):
        return self._get_data_percentage(self.js_data, 'datapoints')

    def _get_performace_data(self, data: DefaultDict[str, List[_ActivityPerHourData]]):
        data_by_actions = self._get_data_total(data, 'actions')
        data_by_datapoints = self._get_data_total(data, 'datapoints')
        return np.divide(data_by_actions, data_by_datapoints, np.zeros_like(data_by_actions, dtype=float), where=data_by_datapoints > 0)

    @property
    def total_performance_per_hour(self):
        return self._get_performace_data(self.total_data)

    @property
    def python_performance_per_hour(self):
        return self._get_performace_data(self.python_data)
               
    @property
    def js_performance_per_hour(self):
        return self._get_performace_data(self.js_data)
