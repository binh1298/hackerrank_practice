from fractions import Fraction
from functools import reduce

standard_input = """3
1 2
3 4
10 6"""


def product(fracs):
    t = reduce(lambda acc, val: acc * val, fracs)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
