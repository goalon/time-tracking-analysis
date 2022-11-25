from statistics.ProjectsPerDays import ProjectsPerDays
from .PseudoHistogram import PseudoHistogram
from .Helper import Helper


class ProjectsWithinOneDay(PseudoHistogram):
    def __init__(self, data: ProjectsPerDays):
        x = range(len(data.projects_per_day_total_percentage))

        super().__init__(
            data=[data.projects_per_day_total_percentage],
            title="Projects within one day of one person",
            xlabel="number of distinct projects",
            ylabel="% of days",
            xticks=Helper.get_simple_bin_xticks(x, last_bin_inf=True),
            percentage=True,
            save_id='projects-day',
        )
