import numpy as np
from numpy.typing import NDArray

def create_alias_table(probs: NDArray):
    n = len(probs)
    scaled_probs = probs * n
    alias = np.zeros(n, dtype=int)
    small = []
    large = []

    for i, sp in enumerate(scaled_probs):
        if sp < 1:
            small.append(i)
        else:
            large.append(i)

    while small and large:
        s = small.pop()
        l = large.pop()

        alias[s] = l
        scaled_probs[l] -= (1 - scaled_probs[s])

        if scaled_probs[l] < 1:
            small.append(l)
        else:
            large.append(l)

    return alias, scaled_probs

def pick(alias: NDArray, scaled_probs: NDArray):
    n = len(alias)
    i = np.random.randint(n)
    r = np.random.rand()

    if r < scaled_probs[i]:
        return i
    else:
        return alias[i]


def pick_from_prob_dist_alias(probs: NDArray):
    """
    preprocess the probabilities to create an alias table, then use it to pick an index in O(1) time.
    """
    
    alias, scaled_probs = create_alias_table(probs)

    return pick(alias, scaled_probs)
