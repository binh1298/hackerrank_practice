from collections import defaultdict


standard_input = """5 2
a
a
b
a
b
a
b"""

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    word = input()
    d[word].append(i + 1)

for i in range(m):
    word = input()
    if (len(d[word]) <= 0):
        print(-1)
    else:
        [print(i, end=" ") for i in d[word]]
        print()
