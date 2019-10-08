import sys
input = lambda: sys.stdin.readline().rstrip()

sys.stdin = open('input.txt', 'r')

n, m, q = map(int, input().split())
logs = [input().split() for _ in range(q)]
score = [{'team': i+1, 'cnt': 0, 'total': 0, 'quiz': [[0, 0] for _ in range(m)]} for i in range(n)]

for log in logs:
    team = int(log[1]) - 1
    num = int(log[2]) - 1
    if log[3] == 'AC':
        # 아직 안 푼 문제일 때
        if score[team]['quiz'][num][1] == 0:
            # 총 시간 = 오답*20 + 통과시간
            score[team]['total'] += score[team]['quiz'][num][0]*20 + int(log[0])
            # 정답 수 증가
            score[team]['cnt'] += 1
            # 완료
            score[team]['quiz'][num][1] = 1
    elif log[3] != 'AC':
        # 오답 수 증가
        score[team]['quiz'][num][0] += 1

score.sort(key=lambda obj: (-obj['cnt'], obj['total'], obj['team']))

for case in score:
    print(case['team'], end=' ')
    print(case['cnt'], end=' ')
    print(case['total'])
