from plotters.PseudoHistogram import PseudoHistogram
from statistics.DelToAdd import DelToAdd as DelToAddStats
from .Helper import Helper
from statistics.Helper import Helper as StatsHelper


class DelToAdd(PseudoHistogram):
    def __init__(self, data: DelToAddStats):
        super().__init__(
            data=[data.del_to_add_per_datapoint, data.del_to_add_per_day],
            title="Deletions to additions ratio",
            xlabel="percentage range",
            ylabel="deletions to additions ratio [%]",
            xticks=Helper.get_range_bin_xticks(StatsHelper.del_to_add_bins * 100),
            percentage=True,
            legend=['per data point', 'per day'],
        )
