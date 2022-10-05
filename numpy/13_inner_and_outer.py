import numpy as np

standard_input = """0 1
2 3"""

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

print(np.inner(A, B))
print(np.outer(A, B))
