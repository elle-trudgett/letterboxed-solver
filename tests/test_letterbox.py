from src.letterbox import LetterBox
from src.side import Side


def test_contains_letters():
    box: LetterBox = LetterBox.from_string("ABC DEF GHI JKL")

    assert box.contains_letters("POPPY") is False, (
        "None of the letters of 'POPPY' are in 'ABC DEF GHI JKL'"
    )
    assert box.contains_letters("DOG") is False, (
        "Only some of the letters of 'DOG' are in 'ABC DEF GHI JKL'"
    )
    assert box.contains_letters("BADGE") is True, (
        "All of the letters of 'BADGE' are in 'ABC DEF GHI JKL'"
    )


def test_from_string():
    box: LetterBox = LetterBox.from_string("ABC DEF GHI JKL")

    assert len(box.sides) == 4, "Box should have 4 sides"
    assert Side("abc") in box.sides, "Box should have an 'ABC' side"
    assert Side("def") in box.sides, "Box should have an 'DEF' side"
    assert Side("ghi") in box.sides, "Box should have an 'GHI' side"
    assert Side("jkl") in box.sides, "Box should have an 'JKL' side"
