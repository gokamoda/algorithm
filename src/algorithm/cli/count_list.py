from algorithm.count import (
    count_by_counter_list_v1,
    count_by_counter_list_v2,
    count_by_counter_list_v3,
    count_by_counter_list_v4,
    count_by_defaultdict_list,
)
from algorithm.data import generate_random_string
from utils.logger import init_logging
from tqdm import tqdm

logger = init_logging(__name__)

count_methods = [
    count_by_counter_list_v1,
    count_by_counter_list_v2,
    count_by_counter_list_v3,
    count_by_counter_list_v4,
    count_by_defaultdict_list,
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

    for _ in tqdm(range(n_iter), desc="Iterations"):
        s = [generate_random_string(string_length) for _ in range(list_size)]
        for method in count_methods:
            with logger.timer(f"{method.__name__}", verbose=False) as t:
                method(s)
            stopwatch[method.__name__] = stopwatch.get(method.__name__, []) + [
                t.elapsed
            ]

    ranking = sorted(stopwatch.items(), key=lambda x: sum(x[1]) / len(x[1]))
    

    return ranking


def main_cli():
    args = parse_args()
    ranking = main(args.n_iter, args.string_length, args.list_size)

    print("Ranking of counting methods:")
    for method_name, times in ranking:
        avg_time = sum(times) / len(times)
        print(f"{method_name}: {avg_time:.6f} seconds (average over {len(times)} runs)")
