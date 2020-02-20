score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
total = 0

while len(score):
    if score[0] >= 80:
        total += score.pop(0)
    else:
        score.pop(0)

print(total)
