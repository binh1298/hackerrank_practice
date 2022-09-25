import numpy
numpy.set_printoptions(legacy="1.13")

standard_input = """1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9"""

original = numpy.array(input().split(), float)

print(numpy.floor(original))
print(numpy.ceil(original))
print(numpy.rint(original))
