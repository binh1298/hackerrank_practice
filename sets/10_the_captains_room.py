k = input()
a = input().split()

roomMap = {}
for i in a:
    if (i in roomMap):
        roomMap[i] += 1
    else:
        roomMap[i] = 1

for i in a:
    if (roomMap[i] == 1):
        print(i)
