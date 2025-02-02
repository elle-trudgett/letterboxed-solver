from typing import Iterable

from src.side import Side, LETTERS_PER_SIDE
from src.utils import upper_alpha

BOX_SIDES = 4


class LetterBox:
    _sides: list[Side]
    _letters: set[str]

    def __init__(self, sides: Iterable[Side]) -> None:
        self._sides = list(sides)
        self._letters = set()

        assert len(self._sides) == BOX_SIDES

        for side in self._sides:
            self._letters |= side.letters

    @property
    def letters(self):
        return tuple(self._letters)

    @property
    def sides(self):
        return list(self._sides)

    def __str__(self):
        return "\n".join(
            [f"Side {x + 1}: {self._sides[x]}" for x in range(len(self._sides))]
        )

    def contains_letters(self, word: str) -> bool:
        word = upper_alpha(word)
        for letter in word:
            if letter not in self._letters:
                return False
        return True

    @classmethod
    def from_string(cls, letters: str) -> "LetterBox":
        letters = upper_alpha(letters)
        assert len(letters) == BOX_SIDES * LETTERS_PER_SIDE
        sides: list[Side] = []
        for i in range(BOX_SIDES):
            sides.append(
                Side(
                    letters[
                        i * LETTERS_PER_SIDE : i * LETTERS_PER_SIDE + LETTERS_PER_SIDE
                    ]
                )
            )
        return cls(sides)
