from statistics.Projects import Projects
from .PseudoHistogram import PseudoHistogram
from .Helper import Helper


class ProjectsPerUser(PseudoHistogram):
    def __init__(self, data: Projects):
        x = range(len(data.projects_per_user_percentage))

        super().__init__(
            data=[data.projects_per_user_percentage],
            title="Projects of one person",
            xlabel="number of distinct projects",
            ylabel="% of people",
            xticks=Helper.get_simple_bin_xticks(x, last_bin_inf=True),
            percentage=True,
            save_id='projects-one-person',
        )
