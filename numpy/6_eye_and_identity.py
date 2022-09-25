import numpy
numpy.set_printoptions(legacy='1.13')

standard_input = """3 3"""
n, m = map(int, input().split())

print(numpy.eye(n, m))
