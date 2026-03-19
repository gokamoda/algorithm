from tqdm import tqdm

from algorithm.data import generate_probability_distribution
from algorithm.random_pick import (
    pick_from_prob_dist_precumsum,
    pick_from_prob_dist_precumsum_bisearch,
    pick_from_prob_dist_simple,
    pick_from_prob_dist_numpy,
    pick_from_prob_dist_alias,
)
from utils.logger import init_logging

logger = init_logging(__name__)

count_methods = [
    pick_from_prob_dist_simple,
    pick_from_prob_dist_precumsum,
    pick_from_prob_dist_precumsum_bisearch,
    pick_from_prob_dist_numpy,
    pick_from_prob_dist_alias,
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
        "--n-types",
        type=int,
        default=128,
        help="Number of types to be generated.",
    )
    return parser.parse_args()


def main(n_iter: int, n_types: int):

    stopwatch = {}

    for _ in tqdm(range(n_iter), desc="Iterations"):
        s = generate_probability_distribution(n_types)
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
    ranking = main(args.n_iter, args.n_types)

    print("Ranking of counting methods:")
    for method_name, times in ranking:
        avg_time = sum(times) / len(times)
        print(f"{method_name}: {avg_time:.6f} seconds (average over {len(times)} runs)")
