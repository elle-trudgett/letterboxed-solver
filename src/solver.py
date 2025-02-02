from src.dictionary import Dictionary
from src.letterbox import LetterBox
from src.solution import Solution


class Solver:
    @classmethod
    def find_solutions(cls, dictionary: Dictionary, box: LetterBox) -> list[Solution]:
        dictionary: Dictionary = dictionary.copy()
        dictionary.prune(box)

        return []
