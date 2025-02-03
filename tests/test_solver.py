from pytest import fixture

from src.dictionary import Dictionary
from src.letterbox import LetterBox
from src.solution import Solution
from src.solver import Solver


@fixture
def simple_dictionary() -> Dictionary:
    dictionary: Dictionary = Dictionary()
    dictionary.add("glow")
    dictionary.add("gospel")
    dictionary.add("slowpoke")
    dictionary.add("golf")
    dictionary.add("flog")
    dictionary.add("foghorns")

    return dictionary


@fixture
def simple_box() -> LetterBox:
    return LetterBox.from_string("RWG ONE FSH PLK")


# @pytest.mark.skip(reason="Solver not implemented.")
def test_find_solutions(simple_dictionary: Dictionary, simple_box: LetterBox):
    solver: Solver = Solver(simple_dictionary, simple_box)
    solutions: list[Solution] = list(solver.solutions())

    print(solutions)

    # Solution on January 1, 2025
    assert Solution(["FOGHORNS", "SLOWPOKE"]) in solutions, "Solution not found"
