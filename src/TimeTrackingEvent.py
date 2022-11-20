from typing import Optional
from datetime import datetime
from collections import defaultdict


class TimeTrackingEventFoundation:
    def __init__(self, data: Optional[dict] = None):
        if data:
            self.additions = data['additions']
            self.deletions = data['deletions']
            self.actions = data['actions']
        else:
            self.additions = 0
            self.deletions = 0
            self.actions = 0
    
    def add(self, data: 'TimeTrackingEventFoundation'):
        self.additions += data.additions
        self.deletions += data.deletions
        self.actions += data.actions


class TimeTrackingEvent(TimeTrackingEventFoundation):
    def __init__(self, author: str, bucket_day: datetime, data: dict):
        super().__init__(data)

        self.author = author
        self.day_bucket = bucket_day

        self.workspace_name_hash = data['workspaceNameHash']

        self.start = datetime.fromisoformat(data['start'])
        self.end = datetime.fromisoformat(data['end'])
        
        self.languages = defaultdict(TimeTrackingEventFoundation)
        for lang, lang_data in data['languages'].items():
            self.languages[lang] = TimeTrackingEventFoundation(lang_data)

    @property
    def contains_python(self):
        return 'python' in self.languages

    @property
    def python_data(self):
        return self.languages['python']

    @property
    def contains_js(self):
        return 'javascript' in self.languages or 'typescript' in self.languages

    @property
    def js_data(self):
        total = TimeTrackingEventFoundation()
        total.add(self.languages['javascript'])
        total.add(self.languages['typescript'])
        return total

    def diff_from_start(self, last_end: datetime) -> float:
        return (self.start - last_end).total_seconds()
