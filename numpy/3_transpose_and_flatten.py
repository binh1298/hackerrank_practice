import numpy
standard_input = """2 2
1 2
3 4"""

n, m = map(int, input().split())

original = numpy.array([list(map(int, input().split())) for _ in range(n)])
transposed = numpy.transpose(original)
flatten = original.flatten()
print(transposed)
print(flatten)
