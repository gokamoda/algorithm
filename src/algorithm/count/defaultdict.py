from collections import defaultdict


def count_by_defaultdict(s: str) -> dict:
    c = defaultdict(int)
    for char in s:
        c[char] += 1
    return dict(c)

def count_by_defaultdict_list(s: list[str]) -> dict:
    c = defaultdict(int)
    for string in s:
        for char in string:
            c[char] += 1
    return dict(c)