height, width = map(int, input().split())
for i in range(1, height - 1, 2):
    line = "".join([".|." for j in range(i)])
    print(line.center(width, "-"))

print("WELCOME".center(width, "-"))

for i in range(height - 2, 0, -2):
    line = "".join([".|." for j in range(i)])
    print(line.center(width, "-"))
