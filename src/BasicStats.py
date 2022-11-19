import os
import jsonlines
from collections import defaultdict
from datetime import datetime
from pathlib import Path


DATA_PATH = '../data'
# DATA_PATH = './data'


class BasicStats:
    def __init__(self):
        self.participants_ids = os.listdir(DATA_PATH)
        self.participants_num = len(self.participants_ids)
        self.participants_stats = {} # todo better init
        self.time = defaultdict(lambda : defaultdict(int))
        self.breaks = {'python': [], 'javascript': []}
        self.del_to_add = {'python': [], 'javascript': []}
        self._count_days()
        self._count_additions_deletions()
        self._gen_data_statistics()
        
    def _count_days(self):
        for pid in self.participants_ids:
            days = 0
            for dirpath, dirnames, filenames in os.walk(os.path.join(DATA_PATH, pid)):
                days += len(filenames)
            self.participants_stats[pid] = {'days': days}
    
    def _count_additions_deletions(self):
        for pid in self.participants_ids:
            additions = 0
            deletions = 0
            actions = 0
            for dirpath, dirnames, filenames in os.walk(os.path.join(DATA_PATH, pid)):
                for filename in filenames:
                    end = {'python': None, 'javascript': None}
                    with jsonlines.open(f'{dirpath}/{filename}') as reader:
                        for obj in reader:
                            additions += obj['additions']
                            deletions += obj['deletions']
                            actions += obj['deletions']
                            hour = obj['start'][11:13]
                            for lang in obj['languages'].keys():
                                self.time[lang][hour] += obj['languages'][lang]['actions']
                            for lang in ['javascript', 'python']:
                                if lang in obj['languages'].keys():
                                    if end[lang]:
                                        start = datetime.fromisoformat(obj['start'])
                                        self.breaks[lang].append((start - end[lang]).total_seconds())
                                    end[lang] = datetime.fromisoformat(obj['end'])
                                    
                                    if obj['languages'][lang]['additions'] > 0:
                                        self.del_to_add[lang].append(obj['languages'][lang]['deletions'] / obj['languages'][lang]['additions'] * 100)
                                    else:
                                        self.del_to_add[lang].append(300)

            self.participants_stats[pid]['additions'] = additions
            self.participants_stats[pid]['deletions'] = deletions
            self.participants_stats[pid]['actions'] = actions

    def _gen_data_statistics(self):
        for pid in self.participants_ids:
            weekdays = defaultdict(int)
            projects = defaultdict(int)
            projects_in_days = []
            switching_projects_in_days = []
            languages = set()
            for dirpath, dirnames, filenames in os.walk(os.path.join(DATA_PATH, pid)):
                for filename in filenames:
                    projects_in_day = set()
                    switching_projects_in_day = 0
                    last_project_name_hash = None
                    year, month = Path(dirpath).parts[-2:]
                    day = Path(filename).stem
                    weekday = datetime(int(year), int(month), int(day)).weekday()
                    with jsonlines.open(f'{dirpath}/{filename}') as reader:
                        for obj in reader:
                            languages.update(obj['languages'].keys())
                            weekdays[weekday] += 1
                            if obj['workspaceNameHash']:
                                projects[obj['workspaceNameHash']] += 1
                                projects_in_day.add(obj['workspaceNameHash'])
                                if last_project_name_hash != obj['workspaceNameHash']:
                                    if last_project_name_hash:
                                        switching_projects_in_day += 1
                                    last_project_name_hash = obj['workspaceNameHash']
                    projects_in_days.append(len(projects_in_day))
                    switching_projects_in_days.append(switching_projects_in_day)
            self.participants_stats[pid]['projects'] = projects
            self.participants_stats[pid]['projects_in_days'] = projects_in_days
            self.participants_stats[pid]['switching_projects_in_days'] = switching_projects_in_days
            self.participants_stats[pid]['weekdays'] = [weekdays[i] for i in range(7)]
            self.participants_stats[pid]['languages'] = languages


# bs = BasicStats()
# print(bs.participants_stats)
