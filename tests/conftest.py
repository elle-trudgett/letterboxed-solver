from _pytest.fixtures import fixture

from src.side import Side


@fixture
def side_abc() -> Side:
    return Side("abc")
