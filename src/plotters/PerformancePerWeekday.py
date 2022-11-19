from plotters.PseudoHistogram import PseudoHistogram
from statistics.Weekdays import Weekdays
from .Helper import Helper


class PerformancePerWeekday(PseudoHistogram):
    def __init__(self, data: Weekdays):
        super().__init__(
            data=[data.actions_per_data_point_per_weekday],
            title="Weekdays performance",
            xlabel="Weekdays performance",
            ylabel="avg. actions per datapoint",
            xticks=Helper.weekdays_xticks,
        )
