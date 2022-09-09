a = set(input().split())
n = int(input())

result = []
for i in range(n):
    s = set(input().split())
    if (len(s.difference(a)) > 0):
        result.append(False)
        continue

    if (len(s) == len(a)):
        result.append(False)
        continue

    result.append(True)

if (False in result):
    print(False)
else:
    print(True)
