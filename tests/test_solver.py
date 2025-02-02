import pytest

from src.dictionary import Dictionary
from src.letterbox import LetterBox
from src.solution import Solution
from src.solver import Solver


@pytest.mark.skip(reason="Solver not implemented.")
def test_find_solutions():
    dictionary: Dictionary = Dictionary()
    dictionary.add("glow")
    dictionary.add("gospel")
    dictionary.add("slowpoke")
    dictionary.add("golf")
    dictionary.add("flog")
    dictionary.add("foghorns")

    box: LetterBox = LetterBox.from_string("RWG ONE FSH PLK")

    solutions: list[Solution] = Solver.find_solutions(dictionary, box)

    # Solution on January 1, 2025
    assert Solution(["FOGHORNS", "SLOWPOKE"]) in solutions, "Solution not found"
