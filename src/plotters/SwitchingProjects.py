from statistics.SwitchingProjects import SwitchingProjects as SwitchingProjectsStats
from .PseudoHistogram import PseudoHistogram
from .Helper import Helper


class SwitchingProjects(PseudoHistogram):
    def __init__(self, data: SwitchingProjectsStats):
        x = range(len(data.switching_projects_per_day_total_percentage))

        super().__init__(
            data=[data.switching_projects_per_day_total_percentage],
            title="Projects switching within one day",
            xlabel="number of switching distinct projects",
            ylabel="% of days",
            xticks=Helper.get_simple_bin_xticks(x, last_bin_inf=True),
            percentage=True,
            save_id='projects-switching-day',
        )
