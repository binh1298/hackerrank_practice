import numpy


def arrays(arr):
    return (numpy.array(arr[::-1], float))


standard_input = """1 2 3 4 -8 -10"""
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
