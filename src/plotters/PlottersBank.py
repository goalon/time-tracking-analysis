from statistics.StatisticsBank import StatisticsBank
from .ProjectsWithinOneDay import ProjectsWithinOneDay
from .ProjectsPerUser import ProjectsPerUser
from .SwitchingProjects import SwitchingProjects
from .ActivityPerWeekday import ActivityPerWeekday
from .PerformancePerWeekday import PerformancePerWeekday
from .DelToAdd import DelToAdd
from .DelToAddLangs import DelToAddLangs
from .Breaks import Breaks
from .ActivityPerHour import ActivityPerHour
from .PerformancePerHourLangs import PerformancePerHourLangs
from .PerformancePerHourTotal import PerformancePerHourTotal


class PlottersBank:
    def __init__(self):
        self._statistics_bank = StatisticsBank()

        self.projects_within_one_day = ProjectsWithinOneDay(self._statistics_bank.projects_per_days)
        self.projects_per_user = ProjectsPerUser(self._statistics_bank.projects)
        self.switching_projects = SwitchingProjects(self._statistics_bank.switching_projects)
        self.activity_per_weekday = ActivityPerWeekday(self._statistics_bank.weekdays)
        self.performance_per_weekday = PerformancePerWeekday(self._statistics_bank.weekdays)
        self.del_to_add = DelToAdd(self._statistics_bank.del_to_add)
        self.del_to_add_langs = DelToAddLangs(self._statistics_bank.del_to_add)
        self.breaks = Breaks(self._statistics_bank.breaks)
        self.activity_per_hour = ActivityPerHour(self._statistics_bank.activity_per_hour)
        self.performance_per_hour_langs = PerformancePerHourLangs(self._statistics_bank.activity_per_hour)
        self.performance_per_hour_total = PerformancePerHourTotal(self._statistics_bank.activity_per_hour)
