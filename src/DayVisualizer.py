from datetime import datetime
from typing import List, Optional
import os
import jsonlines
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.dates import ConciseDateFormatter, HourLocator
from TimeTrackingEvent import TimeTrackingEvent


class DayVisualizer:
    def __init__(self, author: str, date: datetime, participant_no: int):
        self.events: List[TimeTrackingEvent] = []
        self.title_extension = f"of the participant {participant_no} on {date.strftime('%d %b %Y')}"

        data_file_path = os.path.join('..', 'data', author, 'data', str(date.year), str(date.month), f'{date.day}.jsonl')
        with jsonlines.open(data_file_path) as reader:
            for raw_data_point in reader:
                self.events.append(TimeTrackingEvent(author, date, raw_data_point))

        self._generate_data_to_visualize()

    def show_add_and_del(self, save_id: Optional[str] = None):
        self._prepare_show(f"Additions and deletions {self.title_extension}", "time", "avg. no. of chars per second",
                           [self.additions, self.deletions], ["$f_{additions}$", "$-f_{deletions}$"])
        plt.yscale('symlog')
        
        if save_id:
            plt.savefig(os.path.join('..', 'graphics', f'{save_id}.png'), bbox_inches='tight')

        plt.show()

    def show_actions(self, save_id: Optional[str] = None):
        self._prepare_show(f"Actions {self.title_extension}", "time", "avg. no. of actions per second",
                           [self.actions], ["$f_{actions}$"])
        plt.ylim((0, 6))

        if save_id:
            plt.savefig(os.path.join('..', 'graphics', f'{save_id}.png'), bbox_inches='tight')

        plt.show()

    def _generate_data_to_visualize(self):
        self.additions = []
        self.deletions = []
        self.actions = []
        self.datetimes = []

        for event in self.events:
            if event.end != event.start:
                event_length = (event.end - event.start).total_seconds()
            else:
                event_length = 0.001
            
            self.additions.extend(self._generate_step_values(event.additions, event_length))
            self.deletions.extend(self._generate_step_values(-event.deletions, event_length))
            self.actions.extend(self._generate_step_values(event.actions, event_length))

            start = np.datetime64(event.start.isoformat()[:-6])
            end = np.datetime64(event.end.isoformat()[:-6])
            self.datetimes.extend([start, start, end, end])

    @staticmethod
    def _generate_step_values(raw_value: float, event_length: float):
        value = raw_value / event_length
        return [0, value, value, 0]

    def _prepare_show(self, title: str, xlabel: str, ylabel: str, data: list, labels: List[str]):
        plt.figure(figsize=(14, 7))
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.gca().xaxis.set_major_formatter(ConciseDateFormatter(HourLocator()))
        
        for d, label in zip(data, labels):
            plt.plot(self.datetimes, d, label=label)

        plt.legend()
