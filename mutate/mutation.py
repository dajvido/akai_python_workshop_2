import os
import sys
import shutil
import random
import difflib


def test(filename):
    """ for a mutation to pass, it must be a valid python program,
        and test suite must pass,
        yet program is different from original.

        here assume py.test discovers all the tests automatically """
    rv = os.system("python -m py_compile %s 2>/dev/null" % filename)
    # rv == 0 means ok
    if rv:
        print("doesn't parse")
        return False
    rv = os.system("py.test -q . >/dev/null")
    # rv == 0 means ok
    print("test return", rv)
    return not rv


def mutate(filename):
    lines = list(open(filename))
    x, y = random.sample(range(len(lines)), 2)
    lines[x], lines[y] = lines[y], lines[x]
    with open(filename, "w") as fout:
        fout.write("".join(lines))


def loop(filename):
    shutil.copy2(filename, "__xx_backup.py")
    try:
        for i in range(100):
            print(".", end="", flush=True)
            mutate(filename)
            if test(filename):
                print("Code mutated but tests still pass!")
                for line in difflib.unified_diff(list(open("__xx_backup.py")),
                                                 list(open(filename))):
                    print(line, end="")
                # one mutant is enough
                break
    finally:
        shutil.copy2("__xx_backup.py", filename)


if __name__ == "__main__":
    loop(sys.argv[1])
