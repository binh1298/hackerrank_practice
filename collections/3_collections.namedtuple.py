from collections import namedtuple

standard_input = """5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   """
n, Student = int(input()), namedtuple('Student', " ".join(input().split()))
print("{:.2f}".format(sum([int(student.MARKS) for student in [Student(*input().split())
      for i in range(n)]]) / n))
