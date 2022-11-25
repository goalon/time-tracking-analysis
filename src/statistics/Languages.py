from collections import defaultdict
from TimeTrackingEvent import TimeTrackingEvent


class Languages():
    def __init__(self):
        self.data = defaultdict(lambda: defaultdict(int))

    def add(self, event: TimeTrackingEvent):
        for lang in event.languages.keys():
            self.data[event.author][lang] += 1

        if event.contains_js:
            self.data[event.author]['js/ts'] += 1

    @property
    def total_data(self):
        total_data = defaultdict(int)
        for user_data in self.data.values():
            for lang, lang_actions in user_data.items():
                total_data[lang] += lang_actions

        return total_data
