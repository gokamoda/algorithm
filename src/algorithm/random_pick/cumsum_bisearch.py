import numpy as np
from numpy.typing import NDArray


def binary_search(arr: NDArray, target: float) -> int:
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def pick_from_prob_dist_precumsum_bisearch(probs: NDArray):
    r = np.random.rand()

    cumulative_probs = np.cumsum(probs)
    return binary_search(cumulative_probs, r)
