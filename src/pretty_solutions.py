from typing import Iterable

from src.solution import Solution


def pretty_solutions(solutions: Iterable[Solution]) -> Iterable[Solution]:
    solution_bucket: list[Solution] = []
    seen_words: set[Solution] = set()

    solution_size: int | None = None

    for solution in solutions:
        solution_bucket.append(solution)
        if solution_size is None:
            solution_size = len(solution)
        elif len(solution) > solution_size:
            solution_bucket.sort(
                key=lambda s: (s.total_letters, s.max_word_size_difference)
            )

            for soln in solution_bucket:
                soln_word_set = set(soln.words)
                if seen_words & soln_word_set:
                    # Seen words before
                    continue
                seen_words |= soln_word_set
                yield soln

            solution_size = len(solution)
            solution_bucket.clear()
