import random

import numpy as np


def generate_random_string(length: int) -> str:
    letters = "abcdefghijklmnopqrstuvwxyz"
    return "".join(random.choice(letters) for _ in range(length))


def generate_probability_distribution(n: int) -> list[float]:
    """Generate a random probability distribution of size n."""
    probs = np.random.rand(n)
    return probs / np.sum(probs)
