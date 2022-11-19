from collections import defaultdict
import numpy as np
from TimeTrackingEvent import TimeTrackingEvent

class Projects:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, event: TimeTrackingEvent):
        if event.workspace_name_hash:
            self.data[event.author].add(event.workspace_name_hash)

    @property
    def projects_per_user_percentage(self):
        LIMIT = 6

        raw_projects_num_per_users = [len(user_projects) for user_projects in self.data.values()]
        bins = np.concatenate((np.arange(LIMIT + 1), [np.inf]))
        projects_num_per_users = np.histogram(raw_projects_num_per_users, bins)[0]

        return projects_num_per_users / projects_num_per_users.sum()
