from deneme.add import add
import pytest

@pytest.mark.parametrize("x, y", [(1, 2), (3, 4), (5, 6)])
def test_add(x, y):
    assert add(x, y) == x + y
