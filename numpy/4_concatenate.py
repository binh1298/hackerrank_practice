import numpy
standard_input = """4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4"""

n, m, p = map(int, input().split())

firstArray = numpy.array([list(map(int, input().split())) for _ in range(n)])
secondArray = numpy.array([list(map(int, input().split())) for _ in range(m)])

print(numpy.concatenate((firstArray, secondArray), axis=0))
