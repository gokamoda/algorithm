from algorithm.count import (
    count_by_counter_list_v1,
    count_by_counter_list_v2,
    count_by_counter_list_v3,
)
from algorithm.data import generate_random_string
from utils.logger import init_logging

logger = init_logging(__name__)

count_methods = [
    count_by_counter_list_v1,
    count_by_counter_list_v2,
    count_by_counter_list_v3,
]


def parse_args():
    import argparse

    parser = argparse.ArgumentParser(description="Count characters in a string.")
    parser.add_argument(
        "--n-iter",
        type=int,
        default=10,
        help="Number of iterations to run the counting methods.",
    )
    parser.add_argument(
        "--string-length",
        type=int,
        default=128,
        help="Length of the string to be counted.",
    )
    parser.add_argument(
        "--list-size",
        type=int,
        default=256,
        help="Number of strings in the list to be counted.",
    )
    return parser.parse_args()


def main(n_iter: int, string_length: int, list_size: int):

    stopwatch = {}

    for _ in range(n_iter):
        s = [generate_random_string(string_length) for _ in range(list_size)]
        for method in count_methods:
            with logger.timer(f"{method.__name__}", verbose=False) as t:
                method(s)
            stopwatch[method.__name__] = stopwatch.get(method.__name__, []) + [
                t.elapsed
            ]

    ranking = sorted(stopwatch.items(), key=lambda x: sum(x[1]) / len(x[1]))
    print("Ranking of counting methods:")
    for method_name, times in ranking:
        avg_time = sum(times) / len(times)
        print(f"{method_name}: {avg_time:.6f} seconds (average over {len(times)} runs)")

    return ranking


def main_cli():
    args = parse_args()
    main(args.n_iter, args.string_length, args.list_size)
