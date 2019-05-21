# merge namedtuples
from collections import namedtuple
from functools import reduce
from itertools import chain
from operator import add


def merge_namedtuples(*args):
    cls = namedtuple(''.join(arg.__class__.__name__ for arg in args), reduce(add, (arg._fields for arg in args)))
    return cls(*chain(*args))


A = namedtuple("A", "a b c")
B = namedtuple("B", "d e")
a = A(10, 20, 30)
b = B(40, 50)

ab = merge_namedtuples(a, b)

print(a)
print(b)
print(ab)