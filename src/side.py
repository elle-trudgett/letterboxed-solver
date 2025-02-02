from typing import Any

from src.utils import upper_alpha

LETTERS_PER_SIDE = 3


class Side:
    _letters: set[str]
    _str: str

    def __init__(self, letters: str):
        as_upper = upper_alpha(letters)
        self._letters = set(as_upper)
        self._str = " ".join(as_upper)
        assert len(self._letters) == LETTERS_PER_SIDE

    def contains(self, letter_1: str, letter_2: str) -> bool:
        return (
            upper_alpha(letter_1) in self._letters
            and upper_alpha(letter_2) in self._letters
        )

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Side):
            return self._letters == other._letters
        return False

    @property
    def letters(self) -> set[str]:
        return self._letters

    def __str__(self):
        return self._str

    def __repr__(self):
        return f"Side({self})"

    def valid_word(self, word: str) -> bool:
        for i in range(len(word) - 1):
            if self.contains(word[i], word[i + 1]):
                return False
        return True
