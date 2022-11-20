from collections import defaultdict
from typing import Optional, DefaultDict
import numpy as np
from datetime import datetime
from TimeTrackingEvent import TimeTrackingEvent
from .Helper import Helper


class Breaks:
    def __init__(self):
        self.total_data = defaultdict(list)
        self.python_data = defaultdict(list)
        self.js_data = defaultdict(list)
        self._reset()

    def add(self, event: TimeTrackingEvent):
        if self.last_total_end:
            self.total_data[event.author].append(event.diff_from_start(self.last_total_end))
        self.last_total_end = event.end
        
        if event.contains_python:
            if self.last_python_end:
                self.python_data[event.author].append(event.diff_from_start(self.last_python_end))
            self.last_python_end = event.end
        
        if event.contains_js:
            if self.last_js_end:
                self.js_data[event.author].append(event.diff_from_start(self.last_js_end))
            self.last_js_end = event.end

    def finalize_day(self):
        self._reset()

    def _reset(self):
        self.last_total_end: Optional[datetime] = None
        self.last_python_end: Optional[datetime] = None
        self.last_js_end: Optional[datetime] = None

    def _get_histogram(self, data: DefaultDict[str, list]):
        all_data = np.concatenate(list(data.values()))
        histogram = np.histogram(all_data, Helper.breaks_bins)[0]
        return histogram / histogram.sum()

    @property
    def total_breaks(self):
        return self._get_histogram(self.total_data)

    @property
    def python_breaks(self):
        return self._get_histogram(self.python_data)

    @property
    def js_breaks(self):
        return self._get_histogram(self.js_data)
