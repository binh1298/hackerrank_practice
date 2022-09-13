import itertools

standard_input = """HACK 2"""

s, k = input().split()

for permutation in ["\n".join(sorted(["".join(sorted(list(permutation))) for permutation in itertools.combinations(
        s, int(i))])) for i in range(1, int(k) + 1, 1)]:
    print(permutation)
