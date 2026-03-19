import numpy as np
from numpy.typing import NDArray


def pick_from_prob_dist_precumsum(probs: NDArray):
    r = np.random.rand()

    cumulative_probs = np.cumsum(probs)
    for i, cp in enumerate(cumulative_probs):
        if r < cp:
            return i
    return len(probs) - 1
