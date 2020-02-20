score = [88, 30, 61, 55, 95]

for i in range(0, len(score)):
    if score[i] >= 60:
        print("{}번 학생은 {}점으로 합격입니다.".format(i+1, score[i]))
    else:
        print("{}번 학생은 {}점으로 불합격입니다.".format(i+1, score[i]))
