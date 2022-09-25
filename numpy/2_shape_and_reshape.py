import numpy

standard_input = "1 2 3 4 5 6 7 8 9"
result = numpy.array(list(map(int, input().split())))
result.shape = (3, 3)
print(result)
