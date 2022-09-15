import itertools


standard_input = """4 
a a c d
2"""

n = int(input())
l = input().split()
k = int(input())

c = list(itertools.combinations(l, k))
count = 0
for t in c:
    if ("a" in t):
        count += 1

print(count / len(c))
