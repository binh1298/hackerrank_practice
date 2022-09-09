n = int(input())
s = set(map(int, input().split()))

N = int(input())

for i in range(N):
    commandAndValue = input().split()
    if (len(commandAndValue) == 1):
        s.pop()
        continue
    command, value = commandAndValue

    if (command == "remove"):
        s.remove(int(value))
        continue

    if (command == "discard"):
        s.discard(int(value))
        continue

print(sum(list(s)))
