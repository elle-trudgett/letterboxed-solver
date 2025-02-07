from src.dictionary import Dictionary
from src.letterbox import LetterBox
from src.pretty_solutions import pretty_solutions
from src.solver import Solver

WORDS_FILENAME = "words.txt"


def create_box() -> LetterBox:
    print("Example: cle pvt uoa rgi")
    return LetterBox.from_string(input("Enter letters: "))


def main():
    print("------ Letter Boxed Solver ------")

    dictionary: Dictionary = Dictionary.from_file(WORDS_FILENAME)
    box: LetterBox = create_box()
    solver: Solver = Solver(dictionary, box)

    print("Solving...\n")

    num_solutions: int = 0
    for solution in pretty_solutions(solver.solutions()):
        print(solution)
        num_solutions += 1

        if num_solutions % 5 == 0:
            choice = input("\nShow more solutions? (y/N) ").strip().lower()
            if choice != "y":
                break


if __name__ == "__main__":
    main()
