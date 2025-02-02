from src.solution import Solution


def test_eq():
    assert Solution(["test", "thing"]) == Solution(["TEST", "THING"]), (
        "Solutions with same words should be equal"
    )
