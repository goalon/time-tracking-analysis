import os
import jsonlines
from datetime import datetime
from pathlib import Path
import config
from TimeTrackingEvent import TimeTrackingEvent
from .Projects import Projects
from .ProjectsPerDays import ProjectsPerDays
from .SwitchingProjects import SwitchingProjects
from .Weekdays import Weekdays
from .DelToAdd import DelToAdd
from .Breaks import Breaks
from .ActivityPerHour import ActivityPerHour


class StatisticsBank:
    def __init__(self):
        self._init_data()

        for dirpath, _, filenames in os.walk(os.path.join('..', config.DATA_DIR)):
            if not filenames:
                continue

            user_id, _, year, month = Path(dirpath).parts[-4:]
            for filename in filenames:
                day = Path(filename).stem
                bucket_date = datetime(int(year), int(month), int(day))
                with jsonlines.open(os.path.join(dirpath, filename)) as reader:
                    for obj in reader:
                        event = TimeTrackingEvent(user_id, bucket_date, obj)
                        self._add(event)
                self._finalize_day(user_id)
    
    def _init_data(self):
        self.projects = Projects()
        self.projects_per_days = ProjectsPerDays()
        self.switching_projects = SwitchingProjects()
        self.weekdays = Weekdays()
        self.del_to_add = DelToAdd()
        self.breaks = Breaks()
        self.activity_per_hour = ActivityPerHour()

    def _add(self, event: TimeTrackingEvent):
        self.projects.add(event)
        self.projects_per_days.add(event)
        self.switching_projects.add(event)
        self.weekdays.add(event)
        self.del_to_add.add(event)
        self.breaks.add(event)
        self.activity_per_hour.add(event)

    def _finalize_day(self, user_id: str):
        self.projects_per_days.finalize_day(user_id)
        self.switching_projects.finalize_day(user_id)
        self.del_to_add.finalize_day()
        self.breaks.finalize_day()
