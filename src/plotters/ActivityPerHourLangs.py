from plotters.PseudoHistogram import PseudoHistogram
from statistics.ActivityPerHour import ActivityPerHour as ActivityPerHourStats
from .Helper import Helper


class ActivityPerHourLangs(PseudoHistogram):
    def __init__(self, data: ActivityPerHourStats):
        super().__init__(
            data=[data.python_activity_per_hour_by_datapoints, data.js_activity_per_hour_by_datapoints],
            title="Activity by hour restricted to a language",
            xlabel="hour",
            ylabel="% of datapoints",
            xticks=list(range(24)),
            percentage=True,
            legend=['python', 'js/ts'],
            save_id='activity-by-hour-langs',
        )
