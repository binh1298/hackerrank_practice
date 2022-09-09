m = int(input())
mSet = set(list(input().split()))

n = int(input())
nSet = set(list(input().split()))

result = sorted(list(mSet.difference(
    nSet).union(nSet.difference(mSet))), key=int)

for i in result:
    print(i)
