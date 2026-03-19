import numpy as np
from numpy.typing import NDArray


def pick_from_prob_dist_simple(probs: NDArray):
    r = np.random.rand()

    cumsum = 0
    for i, p in enumerate(probs):
        cumsum += p
        if r < cumsum:
            return i
    return len(probs) - 1
