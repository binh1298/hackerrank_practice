

import itertools


standard_input = """1 2
3 4"""

a = map(int, input().split())
b = map(int, input().split())

[print(test, end=" ") for test in itertools.product(a, b)]
