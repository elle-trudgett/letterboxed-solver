from typing import Any

from src.utils import upper_alpha


class Solution:
    _words: list[str]

    def __init__(self, words: list[str]) -> None:
        self._words = [upper_alpha(word) for word in words]

    def __str__(self):
        return " -> ".join(self._words).upper()

    def __eq__(self, other: Any):
        if isinstance(other, Solution):
            return self._words == other._words
