import itertools

standard_input = """HACK 3"""

s, k = input().split()

for permutation in sorted(
        ["".join(list(permutation)) for permutation in itertools.permutations(s, int(k))]):
    print(permutation)
