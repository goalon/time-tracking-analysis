from statistics.StatisticsBank import StatisticsBank
from .ProjectsWithinOneDay import ProjectsWithinOneDay
from .ProjectsPerUser import ProjectsPerUser
from .SwitchingProjects import SwitchingProjects
from .ActivityPerWeekday import ActivityPerWeekday
from .PerformancePerWeekday import PerformancePerWeekday
from .DelToAdd import DelToAdd


class PlottersBank:
    def __init__(self):
        self._statistics_bank = StatisticsBank()

        self.projects_within_one_day = ProjectsWithinOneDay(self._statistics_bank.projects_per_days)
        self.projects_per_user = ProjectsPerUser(self._statistics_bank.projects)
        self.switching_projects = SwitchingProjects(self._statistics_bank.switching_projects)
        self.activity_per_weekday = ActivityPerWeekday(self._statistics_bank.weekdays)
        self.performance_per_weekday = PerformancePerWeekday(self._statistics_bank.weekdays)
        self.del_to_add = DelToAdd(self._statistics_bank.del_to_add)
