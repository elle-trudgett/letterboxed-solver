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
        yield from self._find_solutions([], set(self._letterbox.letters))

    def _pre_solve(self):
        self._dictionary.prune(self._letterbox)

        # Arrange word list for fast processing
        self._prio_words = []

        for word in self._dictionary:
            word_hash: str = "".join(sorted(list(set(word))))
            self._prio_words.append((len(word_hash), word, set(word)))

        self._prio_words.sort(reverse=True)

    def _find_solutions(
        self, chain: list[str], letters_remaining: set[str]
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
            else:
                yield from self._find_solutions(updated_chain, letters_left)
