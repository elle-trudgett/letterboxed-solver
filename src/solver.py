from typing import Iterator

from src.dictionary import Dictionary
from src.letterbox import LetterBox
from src.solution import Solution


class Solver:
    _dictionary: Dictionary
    _letterbox: LetterBox

    _prio_words: list[tuple[int, str, set[str]]]

    def __init__(self, dictionary: Dictionary, letterbox: LetterBox) -> None:
        self._dictionary = dictionary.copy()
        self._letterbox = letterbox

        self._pre_solve()

    def solutions(self) -> Iterator[Solution]:
        for max_solution_length in range(1, 7):
            yield from self._find_solutions(
                [], max_solution_length, set(self._letterbox.letters)
            )

    def _pre_solve(self):
        self._dictionary.prune(self._letterbox)

        # Arrange word list for fast processing
        self._prio_words = []

        for word in self._dictionary:
            word_hash: str = "".join(sorted(list(set(word))))
            self._prio_words.append((len(word_hash), word, set(word)))

        self._prio_words.sort(reverse=True)

    def _find_solutions(
        self, chain: list[str], max_length: int, letters_remaining: set[str]
    ) -> Iterator[Solution]:
        last_letter: str = chain[-1][-1] if chain else ""

        for num_unique_letters, word, letters_in_word in self._prio_words:
            if last_letter and not word.startswith(last_letter):
                continue  # Consecutive words need to share a linking letter
            if word in chain:
                continue  # Words should never repeat in a solution

            letters_left: set[str] = letters_remaining - letters_in_word

            updated_chain: list[str] = chain[:] + [word]
            if not letters_left:
                yield Solution(updated_chain)
            elif len(updated_chain) < max_length:
                yield from self._find_solutions(updated_chain, max_length, letters_left)
