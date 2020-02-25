scores = [(90, 80), (85, 75), (90, 100)]

for i, score in enumerate(scores):
    total = 0
    for x in score:
        total += x
    print('{}번 학생의 총점은 {}점이고, 평균은 {}입니다.'.format(i+1, total, total/2))
