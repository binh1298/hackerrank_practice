from collections import deque


standard_input = """6
append 1
append 2
append 3
appendleft 4
pop
popleft"""

n = int(input())

newDeQueue = deque()
for i in range(n):
    commandAndValue = input().split()
    if (len(commandAndValue) == 1):
        getattr(newDeQueue, commandAndValue[0])()
    else:
        getattr(newDeQueue, commandAndValue[0])(commandAndValue[1])

print(" ".join(newDeQueue))
