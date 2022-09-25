standard_input = """1 4
x**3 + x**2 + x + 1"""

x, k = map(int, input().split())

print(eval(input()) == k)
