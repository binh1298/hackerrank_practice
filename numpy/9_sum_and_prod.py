import numpy as np


standard_input = """2 2
1 2
3 4"""
n, m = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)])

print(np.prod(np.sum(arr, axis=0)))
