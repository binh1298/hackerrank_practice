students = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
    scores.append(score)

sortedScore = sorted(list(set(scores)))
result = []
for student, score in students:
    if (score == sortedScore[1]):
        result.append(student)

sortedStudent = sorted(result)

for student in sortedStudent:
    print(student)
