Install pytest

```
pip install pytest
```

Run all test cases from a single file

```
py.test test_something.py
```

Automatically discover and run all tests

```
py.test .
```

Run only certain tests

```
py.test test_xxx.py::test_yyy
```

Common command line arguments

```
    -s      Don't capture stdout
    --pdb   Invoke debugger on assertion failure
    -k str  Only tests matching str
```

Automatically re-test when source changes

```
pip install pytest-xdist
py.test -f smth
```
