from plotters.PseudoHistogram import PseudoHistogram
from statistics.ActivityPerHour import ActivityPerHour as ActivityPerHourStats
from .Helper import Helper


class ActivityPerHour(PseudoHistogram):
    def __init__(self, data: ActivityPerHourStats):
        super().__init__(
            data=[data.total_activity_per_hour_by_datapoints, data.total_activity_per_hour_by_actions],
            title="Activity by hour",
            xlabel="hour",
            ylabel="% of datapoints/actions",
            xticks=list(range(24)),
            percentage=True,
            legend=['by data points', 'by actions'],
        )
