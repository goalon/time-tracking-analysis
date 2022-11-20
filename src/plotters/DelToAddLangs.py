from plotters.PseudoHistogram import PseudoHistogram
from statistics.DelToAdd import DelToAdd as DelToAddStats
from .Helper import Helper
from statistics.Helper import Helper as StatsHelper


class DelToAddLangs(PseudoHistogram):
    def __init__(self, data: DelToAddStats):
        super().__init__(
            data=[data.python_del_to_add_per_datapoint, data.js_del_to_add_per_datapoint],
            title="Weekdays activity",
            xlabel="Weekdays activity",
            ylabel="% of datapoints/actions",
            xticks=Helper.get_range_bin_xticks(StatsHelper.del_to_add_bins * 100),
            percentage=True,
            legend=['python', 'js/ts'],
        )
