from plotters.PseudoHistogram import PseudoHistogram
from statistics.Breaks import Breaks as BreaksStats
from .Helper import Helper


class Breaks(PseudoHistogram):
    def __init__(self, data: BreaksStats):
        super().__init__(
            data=[data.total_breaks, data.python_breaks, data.js_breaks],
            title="Distribution of break lengths",
            xlabel="break length range",
            ylabel="% of breaks",
            xticks=Helper.get_breaks_xticks(),
            percentage=True,
            legend=['all', 'python', 'js/ts'],
        )
