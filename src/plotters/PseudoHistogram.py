from typing import Optional, Iterable, Union
from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter


class PseudoHistogram():
    def __init__(self, data: Iterable[Iterable[Union[int, float]]], title: str,
                 xlabel: str, ylabel: str, xticks: list, percentage: bool = False,
                 bar_options: Optional[dict] = None, legend: Optional[list] = None):
        self.data = data
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xticks = xticks
        self.percentage = percentage
        self.bar_options = bar_options if bar_options else {}
        self.legend = legend

    def _load_data(self, x):
        for d in self.data:
            plt.bar(x, d, **self.bar_options)

    def show(self):
        plt.figure(figsize=(14, 7))

        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

        x_len = len(self.data[0])
        x = list(range(x_len))
        self._load_data(x)

        if self.percentage:
            plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

        plt.gca().set_xticks(x, self.xticks)

        if self.legend:
            plt.legend(self.legend)

        plt.show()
