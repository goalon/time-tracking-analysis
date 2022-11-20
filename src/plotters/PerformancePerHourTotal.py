from plotters.PseudoHistogram import PseudoHistogram
from statistics.ActivityPerHour import ActivityPerHour as ActivityPerHourStats


class PerformancePerHourTotal(PseudoHistogram):
    def __init__(self, data: ActivityPerHourStats):
        super().__init__(
            data=[data.total_performance_per_hour],
            title="Weekdays activity",
            xlabel="Weekdays activity",
            ylabel="% of datapoints/actions",
            xticks=list(range(24)),
            # legend=['python', 'js/ts'],
        )
