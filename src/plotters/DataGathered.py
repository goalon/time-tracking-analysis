from plotters.PseudoHistogram import PseudoHistogram
from statistics.DataGathered import DataGathered as DataGatheredStats
from .Helper import Helper


class DataGathered(PseudoHistogram):
    def __init__(self, data: DataGatheredStats):
        date_range, actual_data = data.data_gathered
        super().__init__(
            data=actual_data,
            title="Data gathered by date",
            xlabel="dates (in 2022)",
            ylabel="no. of datapoints",
            xticks=Helper.get_date_xticks(date_range),
            xticks_options={'rotation': 'vertical'},
            legend=[f'Participant {i + 1}' for i in range(len(actual_data))],
            stacked=True,
            extended_colors=True,
            save_id='data-gathered-dates',
        )
