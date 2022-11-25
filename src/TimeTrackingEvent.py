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

    def _get_js_related_data(self):
        js_related_data = []
        for lang, lang_data in self.languages.items():
            if 'javascript' in lang or 'typescript' in lang:
                js_related_data.append(lang_data)

        return js_related_data

    @property
    def contains_js(self):
        return bool(self._get_js_related_data())

    @property
    def js_data(self):
        total = TimeTrackingEventFoundation()
        for d in self._get_js_related_data():
            total.add(d)
        
        return total

    def diff_from_start(self, last_end: datetime) -> float:
        return (self.start - last_end).total_seconds()
