from plotters.PseudoHistogram import PseudoHistogram
from statistics.ActivityPerHour import ActivityPerHour as ActivityPerHourStats


class PerformancePerHourLangs(PseudoHistogram):
    def __init__(self, data: ActivityPerHourStats):
        super().__init__(
            data=[data.python_performance_per_hour, data.js_performance_per_hour],
            title="Performance by hour restricted to a language",
            xlabel="hour",
            ylabel="avg. no. of actions per datapoint",
            xticks=list(range(24)),
            legend=['python', 'js/ts'],
        )
