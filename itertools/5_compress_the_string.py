import itertools


standard_input = "1222311"

s = input()

for result in [f"({len(list(grouper))}, {group})" for group, grouper in itertools.groupby(s)]:
    print(result, end=" ")
