import numpy as np
standard_input = """3 2 1"""
inputTuple = tuple(map(int, input().split()))

print(np.zeros(inputTuple, dtype=np.int))
print(np.ones(inputTuple, dtype=np.int))
