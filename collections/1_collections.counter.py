from collections import Counter


standard_input = """10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50"""

X = int(input())
shoesSizes = list(map(int, input().split()))
N = int(input())
inventory = Counter(shoesSizes)

result = 0
for i in range(N):
    size, amount = map(int, input().split())

    if (inventory[size] <= 0):
        continue

    inventory[size] -= 1
    result += amount

print(result)
