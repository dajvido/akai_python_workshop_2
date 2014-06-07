import pytest
import unittest.mock

from calc import (
    main,
    calculate,
)


def test_simple_add_eq():
    assert(calculate('1+2') == 3.0)


def test_simple_sub_eq():
    assert(calculate('3-2') == 1.0)


def test_simple_mul_eq():
    assert(calculate('2*2') == 4.0)


def test_simple_div_eq():
    assert(calculate('1/2') == 0.5)


def test_simple_power_eq():
    assert(calculate('2^3') == 8.0)


def test_complicated_eq():
    with unittest.mock.patch("random.randint", lambda x, y: 0):
        assert(calculate("1.3+2*3-2^3-5/2+R") == -3.2)


def test_supported_variables():
    with unittest.mock.patch("random.randint", lambda x, y: 0):
        assert(calculate("R+G") == 9.81)


def test_not_supported_variable():
    with pytest.raises(ValueError):
        calculate("Z+5")


def test_validate_eq():
    with pytest.raises(ValueError):
        calculate('3+-5+RR')


def test_valid_operator_at_the_beginning():
    assert(calculate("-5+3") == -2.0)


def test_invalid_operator_at_the_beginning():
    with pytest.raises(ValueError):
        calculate("*5+3")


def test_invalid_operator_at_the_end():
    with pytest.raises(ValueError):
        calculate("5+3+")


def test_invalid_combination():
    with pytest.raises(ValueError):
        calculate("5+-3")


def test_invalid_input_data():
    with pytest.raises(ValueError):
        calculate("")


def test_run_with_arguments(capfd):
    with unittest.mock.patch("sys.argv", ["calc.py", "1+3"]):
        main()
        out, _ = capfd.readouterr()
        assert out.strip() == "4.0"
