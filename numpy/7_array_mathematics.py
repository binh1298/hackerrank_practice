import numpy

standard_input = """1 4
1 2 3 4
5 6 7 8"""

n, m = map(int, input().split())

a = numpy.array([numpy.array(list(map(int, input().split())))
                for _ in range(n)])
b = numpy.array([numpy.array(list(map(int, input().split())))
                for _ in range(n)])

print(numpy.array(a+b))
print(numpy.array(a-b))
print(numpy.array(a*b))
print(numpy.array(numpy.floor_divide(a, b)))
print(numpy.array(a % b))
print(numpy.array(a**b))
