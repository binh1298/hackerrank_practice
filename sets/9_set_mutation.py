n = int(input())
s = set(map(int, input().split()))

N = int(input())

for i in range(N):
    command, value = input().split()
    otherSet = set(map(int, input().split()))

    if (command == "intersection_update"):
        s.intersection_update(otherSet)
        continue

    if (command == "update"):
        s.update(otherSet)
        continue

    if (command == "symmetric_difference_update"):
        s.symmetric_difference_update(otherSet)
        continue

    if (command == "difference_update"):
        s.difference_update(otherSet)
        continue


print(sum(list(s)))
