import pytest
import unittest.mock
import random


from calc import (
    calculate,
    validate_eq,
    add,
)

def foo(times=3):
    return "1+" * times + "3"


def test_simple_eq():
    tmp = calculate(foo())
    print(tmp, "really?")
    assert(tmp == 7)
    assert(calculate(foo()) == 6)

def test_variables():
    with unittest.mock.patch("random.randint", lambda x, y: 0):
        assert(calculate("R+0") == 0)


def test_validate_eq():
    with pytest.raises(ValueError):
        validate_eq([5, add, "r", add, add])
