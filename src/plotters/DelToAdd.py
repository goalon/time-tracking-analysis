from plotters.PseudoHistogram import PseudoHistogram
from statistics.DelToAdd import DelToAdd as DelToAddStats
from .Helper import Helper


class DelToAdd(PseudoHistogram):
    def __init__(self, data: DelToAddStats):
        x = range(len(data.del_to_add_per_datapoint))

        super().__init__(
            data=[data.del_to_add_per_datapoint],
            title="Weekdays activity",
            xlabel="Weekdays activity",
            ylabel="% of datapoints/actions",
            xticks=Helper.get_simple_bin_xticks(x),
            percentage=True,
            # bar_options={'alpha': 0.5},
            # legend=['by data points', 'by actions'],
        )
