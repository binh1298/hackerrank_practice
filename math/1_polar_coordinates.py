import cmath

standard_input = """1+2j"""

z = complex(input())

r = abs(z)
theta = cmath.phase(z)

print(r)
print(theta)
