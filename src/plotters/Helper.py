from typing import Iterable


class Helper:
    @staticmethod
    def get_simple_bin_xticks(x: Iterable[int], last_bin_inf: bool = False):
        xticks = [str(_x) for _x in x]
        if last_bin_inf:
            xticks[-1] = f">={xticks[-1]}"
        
        return xticks
    
    weekdays_xticks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
