import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : queue
# 발상 : enqueue -> dequeue 반복
# 변형 : 피자의 치즈가 녹으면 꺼내고, 안 녹으면 다시 넣음
# 조합 :

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    q = [[i+1, Ci[i]] for i in range(N)]  # 화덕에 피자 채우기
    i = 0

    while len(q) != 1:
        q[0][1] //= 2
        if q[0][1] == 0:
            if N+i < M:  # 꺼내고 다른 피자 넣기
                q.pop(0)
                q.append([N+i+1, Ci[N+i]])
                i += 1
            else:
                q.pop(0)
        else:
            q.append(q.pop(0))

    print('#{} {}'.format(t, q[0][0]))
