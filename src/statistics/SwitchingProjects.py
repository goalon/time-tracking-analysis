from collections import defaultdict
import numpy as np
from TimeTrackingEvent import TimeTrackingEvent


class SwitchingProjects():
    def __init__(self):
        self.data = defaultdict(list)
        self._reset()

    def _reset(self):
        self.last_project = None
        self.counter = 0

    def add(self, event: TimeTrackingEvent):
        if event.workspace_name_hash is None:
            return

        if self.last_project != event.workspace_name_hash:
            if self.last_project:
                self.counter += 1
            self.last_project = event.workspace_name_hash

    def finalize_day(self, author: str):
        self.data[author].append(self.counter)
        self._reset()

    @property
    def switching_projects_per_day_total_percentage(self):
        LIMIT = 5

        switching_projects_per_day = np.zeros(LIMIT + 1)
        bins = np.concatenate((np.arange(LIMIT + 1), [np.inf]))
        for user_switching_projects_per_day in self.data.values():
            switching_projects_per_day += np.histogram(user_switching_projects_per_day, bins)[0]

        return switching_projects_per_day / switching_projects_per_day.sum()
