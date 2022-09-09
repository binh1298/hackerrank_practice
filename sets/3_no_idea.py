n, m = input().split()
numbersSet = list(input().split())
a = set(list(input().split()))
b = set(list(input().split()))

result = 0
for i in numbersSet:
    if (i in a):
        result += 1
    if (i in b):
        result -= 1

print(result)
