n = int(input())
a = [input().split() for _ in range(n)]

a.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in a:
    print(student[0])
