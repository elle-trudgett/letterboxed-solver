from dataclasses import dataclass, field

from src.letterbox import LetterBox
from src.side import Side
from src.utils import upper_alpha


@dataclass
class Dictionary:
    _words: list[str] = field(default_factory=list)

    def add(self, word: str) -> None:
        word = upper_alpha(word)

        if len(word) < 3:
            # Letterboxed doesn't allow 1-2 letter words
            return

        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                # Letterboxed doesn't have words with double letters
                return

        self._words.append(word)

    def prune_side(self, side: Side) -> None:
        self._words = list(filter(lambda w: side.valid_word(w), self._words))

    def prune(self, box: LetterBox) -> None:
        for side in box.sides:
            self.prune_side(side)
        self._words = list(filter(lambda w: box.contains_letters(w), self._words))

    @classmethod
    def from_file(cls, filename: str) -> "Dictionary":
        dictionary: Dictionary = cls()
        with open(filename, "r") as f:
            words = f.readlines()
        for word in words:
            dictionary.add(word)

        return dictionary

    def __contains__(self, word: str) -> bool:
        return upper_alpha(word) in self._words

    def __len__(self) -> int:
        return len(self._words)
