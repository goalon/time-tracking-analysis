from collections import defaultdict
import numpy as np
from TimeTrackingEvent import TimeTrackingEvent


class ProjectsPerDays():
    def __init__(self):
        self.data = defaultdict(list)
        self.projects_per_day = set()

    def add(self, event: TimeTrackingEvent):
        if event.workspace_name_hash:
            self.projects_per_day.add(event.workspace_name_hash)

    def finalize_day(self, author: str):
        self.data[author].append(len(self.projects_per_day))
        self.projects_per_day = set()

    @property
    def projects_per_day_total_percentage(self):
        LIMIT = 5

        projects_per_days = np.zeros(LIMIT + 1)
        bins = np.concatenate((np.arange(LIMIT + 1), [np.inf]))
        for user_projects_per_days in self.data.values():
            projects_per_days += np.histogram(user_projects_per_days, bins)[0]

        return projects_per_days / projects_per_days.sum()
