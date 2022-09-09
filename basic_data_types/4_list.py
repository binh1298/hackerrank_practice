n = int(input())

arr = []
printer = []
for i in range(n):
    commandAndValues = input().split()

    if (commandAndValues[0] == "insert"):
        arr.insert(int(commandAndValues[1]), int(commandAndValues[2]))
        continue

    if (commandAndValues[0] == "print"):
        printer.append([i for i in arr])
        continue

    if (commandAndValues[0] == "remove"):
        arr.remove(int(commandAndValues[1]))
        continue

    if (commandAndValues[0] == "append"):
        arr.append(int(commandAndValues[1]))
        continue

    if (commandAndValues[0] == "sort"):
        arr.sort()
        continue

    if (commandAndValues[0] == "pop"):
        arr.pop()
        continue

    if (commandAndValues[0] == "reverse"):
        arr.reverse()
        continue

for p in printer:
    print(p)
