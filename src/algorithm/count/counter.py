from collections import Counter


def count_by_counter(s: str) -> dict:
    c = Counter(s)
    return dict(c)


def count_by_counter_list_v1(s: list[str]) -> dict:
    """
    Count characters in a list of strings.
    """

    c = Counter()
    for string in s:
        c.update(string)
    return dict(c)


def count_by_counter_list_v2(s: list[str]) -> dict:
    """
    Count characters in a list of strings.
    """

    c = Counter()
    for string in s:
        update_counter = Counter(string)
        c.update(update_counter)
    return dict(c)


def count_by_counter_list_v3(s: list[str]) -> dict:
    """
    Count characters in a list of strings.
    """

    c = Counter()
    for string in s:
        update_counter = Counter(string)
        c += update_counter
    return dict(c)

def count_by_counter_list_v4(s: list[str]) -> dict:
    
    return dict(sum((Counter(string) for string in s), Counter()))