from src.letterbox import LetterBox
from src.dictionary import Dictionary
from src.side import Side


def test_add():
    dictionary: Dictionary = Dictionary()
    dictionary.add("hello")
    dictionary.add("world")

    assert dictionary._words == ["WORLD"], "'HELLO' is not a valid Letterboxed word"


def test_prune_side():
    dictionary: Dictionary = Dictionary()
    dictionary.add("prune")
    dictionary.add("side")

    assert len(dictionary) == 2, "Expected two words in the dictionary"
    assert "prune" in dictionary, "'PRUNE' should be in the dictionary"
    assert "side" in dictionary, "'SIDE' should be in the dictionary"

    dictionary.prune_side(Side("lrp"))
    assert len(dictionary) == 1, "Side 'LRP' should prune word 'PRUNE'"
    assert "side" in dictionary, "Side 'LRP' should prune word 'PRUNE'"

    dictionary.prune_side(Side("sdx"))
    assert len(dictionary) == 1, "Side 'SDX' does not prune word 'SIDE'"
    assert "side" in dictionary, "Side 'SDX' does not prune word 'SIDE'"

    dictionary.prune_side(Side("DEF"))
    assert len(dictionary) == 0, "Side 'DEF' should prune word 'SIDE'"


def test_prune():
    dictionary: Dictionary = Dictionary()
    dictionary.add("balcony")
    dictionary.add("manta")
    dictionary.add("pieces")
    dictionary.add("turnip")

    box: LetterBox = LetterBox.from_string("BAMTRPUICNEW")

    dictionary.prune(box)

    assert len(dictionary) == 1, (
        "The only valid word left for this box should be 'TURNIP'"
    )
    assert "turnip" in dictionary, "'TURNIP' should be in the dictionary"


def test_copy():
    dictionary: Dictionary = Dictionary()
    dictionary.add("echo")
    dictionary.add("foxtrot")

    dictionary_copy = dictionary.copy()

    assert dictionary.words == dictionary_copy.words, "Copied words should be equal"

    dictionary.add("golf")

    assert len(dictionary_copy.words) == 2, (
        "Dictionary copy should not have been modified"
    )

    dictionary_copy.prune_side(Side("FOX"))

    assert len(dictionary.words) == 3, (
        "Original dictionary should not have been modified"
    )
