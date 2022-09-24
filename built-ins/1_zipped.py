standard_input = """5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5"""

numberOfStudents, numberOfSubjects = map(int, input().split())

[print(sum(studentGradesTuple) / numberOfSubjects) for studentGradesTuple in zip(*[map(float, input().split())
                                                                                   for _ in range(numberOfSubjects)])]
