import pytest


def add(x, y):
    return x + y

@add
def test_add():
    assert 3 == add(1, 2)
