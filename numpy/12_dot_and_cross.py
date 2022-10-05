import numpy as np

standard_input = """2
1 2
3 4
1 2
3 4"""

n = int(input())

A = np.array([list(map(int, input().split())) for _ in range(n)])
B = np.array([list(map(int, input().split())) for _ in range(n)])

print(np.dot(A, B))
