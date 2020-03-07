import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Greedy
# 발상 : 전체 부분집합 중에서 n개인 것 골라야 해서
# 변형 : 전체를 탐색하되 조건이 맞는 경우의 수만 비교
# 조합 : 비트 연산자 -> 모든 부분 집합 구할 때

T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    arr = [i for i in range(1, 13)]
    cnt = 0
    for i in range(1 << 12):
        sub = []
        for j in range(12):
            if i & (1 << j):
                sub.append(arr[j])
        if len(sub) == n and sum(sub) == k:
            cnt += 1
    print('#{} {}'.format(t, cnt))
