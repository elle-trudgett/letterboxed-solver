from src.dictionary import Dictionary
from src.letterbox import LetterBox
from src.solution import Solution


class Solver:
    def __init__(self, dictionary: Dictionary) -> None:
        self._dictionary = dictionary

    def find_solutions(self, box: LetterBox) -> list[Solution]:
        self._dictionary.prune(box)

        return []
