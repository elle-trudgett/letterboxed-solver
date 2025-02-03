from typing import Any

from src.utils import upper_alpha


class Solution:
    _words: list[str]

    def __init__(self, words: list[str]) -> None:
        self._words = [upper_alpha(word) for word in words]

    @property
    def words(self) -> list[str]:
        return self._words

    @property
    def total_letters(self) -> int:
        return sum(len(word) for word in self._words)

    @property
    def max_word_size_difference(self) -> int:
        word_sizes = [len(word) for word in self._words]
        return max(word_sizes) - min(word_sizes)

    def __str__(self) -> str:
        return " -> ".join(self._words).upper()

    def __len__(self) -> int:
        return len(self._words)

    def __repr__(self) -> str:
        return f"Solution({self})"

    def __eq__(self, other: Any):
        if isinstance(other, Solution):
            return self._words == other._words
