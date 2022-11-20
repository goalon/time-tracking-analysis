from plotters.PseudoHistogram import PseudoHistogram
from statistics.Weekdays import Weekdays
from .Helper import Helper


class ActivityPerWeekday(PseudoHistogram):
    def __init__(self, data: Weekdays):
        super().__init__(
            data=[data.data_points_per_weekday_percentage, data.actions_per_weekday_percentage],
            title="Weekdays activity",
            xlabel="weekday",
            ylabel="% of datapoints/actions",
            xticks=Helper.weekdays_xticks,
            percentage=True,
            legend=['by data points', 'by actions'],
        )
