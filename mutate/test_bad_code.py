import bad_code


def test_foo():
    rv = bad_code.foo(12, 34)
    assert len(rv) == 2
