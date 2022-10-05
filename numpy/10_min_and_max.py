import numpy as np


standard_input = """4 2
2 5
3 7
1 3
4 0"""
n, m = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)])

print(np.max(np.min(arr, axis=1)))
