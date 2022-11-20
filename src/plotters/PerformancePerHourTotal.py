from plotters.PseudoHistogram import PseudoHistogram
from statistics.ActivityPerHour import ActivityPerHour as ActivityPerHourStats


class PerformancePerHourTotal(PseudoHistogram):
    def __init__(self, data: ActivityPerHourStats):
        super().__init__(
            data=[data.total_performance_per_hour],
            title="Performance by hour",
            xlabel="hour",
            ylabel="avg. no. of actions per datapoint",
            xticks=list(range(24)),
        )
