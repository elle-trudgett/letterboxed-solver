from src.dictionary import Dictionary
from src.letterbox import LetterBox
from src.solution import Solution
from src.solver import Solver


def test_find_solutions():
    dictionary: Dictionary = Dictionary()
    dictionary.add("forge")
    dictionary.add("gospel")
    dictionary.add("slowpoke")
    dictionary.add("golf")

    box: LetterBox = LetterBox.from_string("RWG ONE FSH PLK")

    solver: Solver = Solver(dictionary)

    solutions: list[Solution] = solver.find_solutions(box)

    # Solution on January 1, 2025
    assert Solution(["FOGHORNS", "SLOWPOKE"]) in solutions, "Solution not found"
