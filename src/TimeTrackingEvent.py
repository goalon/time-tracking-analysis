from datetime import datetime


class _TimeTrackingEventFoundation:
    def __init__(self, data: dict):
        self.additions = data['additions']
        self.deletions = data['deletions']
        self.actions = data['actions']


class TimeTrackingEvent(_TimeTrackingEventFoundation):
    def __init__(self, author: str, bucket_day: datetime, data: dict):
        super().__init__(data)

        self.author = author
        self.day_bucket = bucket_day

        self.workspace_name_hash = data['workspaceNameHash']

        self.start = datetime.fromisoformat(data['start'])
        self.end = datetime.fromisoformat(data['end'])
        
        self.languages = {}
        for lang, lang_data in data['languages'].items():
            self.languages[lang] = _TimeTrackingEventFoundation(lang_data)
