import itertools

standard_input = """HACK 2"""

s, k = input().split()

[print(result) for result in sorted(["".join(sorted(test))
                                     for test in itertools.combinations_with_replacement(s, int(k))])]
