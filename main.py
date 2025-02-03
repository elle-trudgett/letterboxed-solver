from src.pretty_solutions import pretty_solutions
from src.solver import Solver
from src.dictionary import Dictionary
from src.letterbox import LetterBox, BOX_SIDES
from src.side import Side, LETTERS_PER_SIDE
from src.utils import upper_alpha

WORDS_FILENAME = "words.txt"


def create_box() -> LetterBox:
    sides: list[Side] = []
    for i in range(BOX_SIDES):
        letters: str = input(f"Enter {LETTERS_PER_SIDE} letters for side {i + 1}: ")
        letters = upper_alpha(letters)
        side = Side(letters=letters)
        sides.append(side)

    return LetterBox(sides=sides)


def main():
    dictionary: Dictionary = Dictionary.from_file(WORDS_FILENAME)
    box: LetterBox = create_box()
    solver: Solver = Solver(dictionary, box)

    num_solutions: int = 0
    for solution in pretty_solutions(solver.solutions()):
        print(solution)
        num_solutions += 1

        if num_solutions % 5 == 0:
            choice = input("Show more solutions? (y/N) ").strip().lower()
            if choice != "y":
                break


if __name__ == "__main__":
    main()
