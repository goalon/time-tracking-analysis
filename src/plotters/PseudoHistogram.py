from typing import Optional, Iterable, Union
import os
from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np


class PseudoHistogram():
    def __init__(self, data: Iterable[Iterable[Union[int, float]]], title: str,
                 xlabel: str, ylabel: str, xticks: Optional[list] = None, xticks_options: Optional[dict] = None,
                 percentage: bool = False, bar_options: Optional[dict] = None, legend: Optional[list] = None,
                 stacked: bool = False, extended_colors: bool = False, save_id: Optional[bool] = None):
        self.data = np.asarray(data)
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xticks = xticks
        self.xticks_options = xticks_options if xticks_options else {}
        self.percentage = percentage
        self.bar_options = bar_options if bar_options else {}
        self.legend = legend
        self.stacked = stacked
        self.extended_colors = extended_colors
        self.save_id = save_id

    def _load_data(self, x):
        ALL_WIDTH = 0.8
            
        if self.stacked:
            bottoms = np.concatenate((np.zeros_like(self.data[:1]), self.data.cumsum(axis=0)[:-1]), axis=0)
            for d, bottom in zip(self.data, bottoms):
                plt.bar(x, d, ALL_WIDTH, bottom, **self.bar_options)
        else:
            width = ALL_WIDTH / len(self.data)
            offset = -ALL_WIDTH / 2 + width / 2
            for d in self.data:
                plt.bar(x + offset, d, width, **self.bar_options)
                offset += width

    def show(self):
        plt.figure(figsize=(14, 7))

        if self.extended_colors:
            plt.gca().set_prop_cycle(color=plt.get_cmap('tab20').colors)

        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

        x_len = len(self.data[0])
        x = np.asarray(list(range(x_len)))
        self._load_data(x)

        if self.percentage:
            plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

        if self.xticks is not None:
            plt.gca().set_xticks(x, self.xticks, **self.xticks_options)

        if self.legend:
            plt.legend(self.legend)

        if self.save_id:
            plt.savefig(os.path.join('..', 'graphics', f'{self.save_id}.png'), bbox_inches='tight')

        plt.show()
