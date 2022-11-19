from collections import defaultdict
import numpy as np
from TimeTrackingEvent import TimeTrackingEvent


class _WeekdayData():
    def __init__(self):
        self.data_points = 0
        self.actions = 0

    def add(self, event: TimeTrackingEvent):
        self.data_points += 1
        self.actions += event.actions


class Weekdays():
    def __init__(self):
        self.data = defaultdict(lambda: [_WeekdayData() for _ in range(7)])

    def add(self, event: TimeTrackingEvent):
        self.data[event.author][event.day_bucket.weekday()].add(event)

    @property
    def _data_points_per_weekday(self):
        data_points_per_weekday = np.zeros(7)
        for weekdays_data in self.data.values():
            user_data_points_per_weekday = [weekday_data.data_points for weekday_data in weekdays_data]
            data_points_per_weekday += np.asarray(user_data_points_per_weekday)

        return data_points_per_weekday

    @property
    def data_points_per_weekday_percentage(self):
        data_points_per_weekday = self._data_points_per_weekday
        return data_points_per_weekday / data_points_per_weekday.sum()

    @property
    def _actions_per_weekday(self):
        actions_per_weekday = np.zeros(7)
        for weekdays_data in self.data.values():
            user_actions_per_weekday = [weekday_data.actions for weekday_data in weekdays_data]
            actions_per_weekday += np.asarray(user_actions_per_weekday)

        return actions_per_weekday

    @property
    def actions_per_weekday_percentage(self):
        actions_per_weekday = self._actions_per_weekday
        return actions_per_weekday / actions_per_weekday.sum()

    @property
    def actions_per_data_point_per_weekday(self):
        return self._actions_per_weekday / self._data_points_per_weekday
