from operator import itemgetter
from plotters.PseudoHistogram import PseudoHistogram
from statistics.Languages import Languages


class LanguagesTotal(PseudoHistogram):
    def __init__(self, data: Languages):
        sorted_items = sorted(data.total_data.items(), key=itemgetter(1), reverse=True)
        languages, languages_datapoints = zip(*sorted_items)

        super().__init__(
            data=[languages_datapoints],
            title="Amount of data gathered by language",
            xlabel="language",
            ylabel="no. of datapoints",
            xticks=languages,
            xticks_options={'rotation': 'vertical'},
            save_id='languages-total',
        )
