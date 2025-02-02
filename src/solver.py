from collections import defaultdict

from src.dictionary import Dictionary
from src.letterbox import LetterBox
from src.solution import Solution


class Solver:
    @classmethod
    def find_solutions(cls, dictionary: Dictionary, box: LetterBox) -> list[Solution]:
        dictionary: Dictionary = dictionary.copy()
        dictionary.prune(box)

        # Hash remaining dictionary words into their unique letters
        unique_word_hash: dict[str, list] = defaultdict(list)
        for word in dictionary:
            word_hash: str = "".join(sorted(list(set(word))))
            unique_word_hash[word_hash].append(word)

        print(unique_word_hash)

        return []
