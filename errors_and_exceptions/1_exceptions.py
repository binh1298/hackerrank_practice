standard_input = """3
1 0
2 $
3 1"""

t = int(input())
for i in range(t):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:", e)
