import timeit
import argparse


def time_them(them):
    for s in (them):
        print("\n=========")
        print(s)
        print("---------")
        print(timeit.timeit(stmt=s, number=1000))
        print("=========")

s1 = """\
x = []
for i in xrange(0, 10000):
    x.append(i)
"""

s2 = "x = [i for i in xrange(0, 10000)]"


s3 = """\
foo = {}
for x in xrange(0, 100):
    for y in xrange(0, 100):
        foo["{}:{}".format(x, y)] = (y, x)
"""

s4 = """\
foo = {}
for x in xrange(0, 100):
    for y in xrange(0, 100):
        foo[":".join([str(x), str(y)])] = (y, x)
"""

s5 = """\
foo = dict()
for x in xrange(0, 100):
    for y in xrange(0, 100):
        foo[(x, y)] = (y, x)
"""


s6 = """\
foo = []
for x in xrange(0, 10000):
    foo.append(x)
"""

s7 = """\
foo = []
foo_append = foo.append
for x in xrange(0, 10000):
    foo_append(x)
"""

sets = {
    'comprehension': [s1, s2],
    'dictkeys': [s3, s4, s5],
    'dots': [s6, s7],
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="run timeit examples"
    )

    parser.add_argument("timeit_set",
                        type=str,
                        help="The timeit set to run")

    args = parser.parse_args()

    if args.timeit_set in sets:
        time_them(sets[args.timeit_set])
    else:
        print('Unknown set"')
