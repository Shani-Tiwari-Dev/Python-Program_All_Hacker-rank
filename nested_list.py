students = []

n = int(input())

for i in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

lowest = students[0][1]
for s in students:
    if s[1] < lowest:
        lowest = s[1]

second_lowest = None
for s in students:
    if s[1] != lowest:
        if second_lowest is None or s[1] < second_lowest:
            second_lowest = s[1]

names = []
for s in students:
    if s[1] == second_lowest:
        names.append(s[0])

names.sort()

for name in names:
    print(name)
