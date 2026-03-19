import random


def generate_random_string(length: int) -> str:
    letters = "abcdefghijklmnopqrstuvwxyz"
    return "".join(random.choice(letters) for _ in range(length))
