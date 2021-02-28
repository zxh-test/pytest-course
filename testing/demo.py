import pytest


def add(x, y):
    return x + y


def test1():
    return 1

def test2(test1):
    print(test1)

test2(test1)