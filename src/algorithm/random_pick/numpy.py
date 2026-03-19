import numpy as np
from numpy.typing import NDArray


def pick_from_prob_dist_numpy(probs: NDArray):
    return np.random.choice(len(probs), p=probs)
