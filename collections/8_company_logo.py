from collections import Counter
import functools


standard_input = """qwertyuiopasdfghjklzxcvbnm"""

s = input()


def comparator(firstTuple, secondTuple):
    firstKey, firstValue = firstTuple
    secondKey, secondValue = secondTuple

    if (firstValue > secondValue):
        return -1

    if (firstValue < secondValue):
        return 1

    if (firstKey > secondKey):
        return 1

    if (firstKey < secondKey):
        return -1

    return -1


[print(f"{i} {j}") for i, j in sorted(Counter(sorted(s)).most_common(
    3), key=functools.cmp_to_key(comparator))]
