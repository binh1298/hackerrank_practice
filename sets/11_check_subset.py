t = int(input())


def checkAIsSubsetOfB(aSet: set, bSet: set):
    return len(aSet.difference(bSet)) == 0


result = []
for i in range(t):
    a = int(input())
    aSet = set(input().split())
    b = int(input())
    bSet = set(input().split())
    result.append(checkAIsSubsetOfB(aSet, bSet))

for r in result:
    print(r)
