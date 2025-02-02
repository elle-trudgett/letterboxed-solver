from src.side import Side


def test_contains(side_abc: Side):
    assert side_abc.contains("a", "b") is True, "Side contains both letters"


def test_does_not_contain(side_abc: Side):
    assert side_abc.contains("a", "x") is False, "Side does not contain one letter"
    assert side_abc.contains("x", "b") is False, "Side does not contain one letter"
    assert side_abc.contains("x", "y") is False, "Side does not contain either letter"


def test_valid_word(side_abc: Side):
    assert side_abc.valid_word("POTATO") is True, (
        "'POTATO' does not contain consecutive letters from 'ABC'"
    )
    assert side_abc.valid_word("BABY") is False, (
        "'BABY' contains consecutive letters from 'ABC'"
    )


def test_eq():
    assert Side("abc") == Side("cab") == Side("bac"), (
        "Sides should be equal regardless of letter order"
    )
    assert Side("abc") in [Side("ABC"), Side("DEF"), Side("GHI"), Side("JKL")], (
        "Side should be found in list"
    )
