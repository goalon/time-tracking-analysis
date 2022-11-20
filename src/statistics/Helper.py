import numpy as np

class Helper:
    del_to_add_bins = np.concatenate((np.arange(0, 3, 0.25), [np.inf]))
    breaks_bins = np.asarray([0, 1, 5, 10, 30, 60, 120, 180, 300, 600, 1800, 3600, 86400])
