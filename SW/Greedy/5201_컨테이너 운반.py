import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Greedy
# 발상 : 적재 용량이 가장 큰 트럭부터 가장 무거운 화물을 나르면 최대 중량 가능
# 변형 : 제한된 적재 용량을 가진 트럭으로 이동한 화물의 총 중량이 최대가 될 때의 총 중량
# 조합 : sort

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    objs = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    ans = 0
    objs.sort(reverse=True)
    trucks.sort(reverse=True)
    i = 0
    for truck in trucks:
        if i < N:
            for j in range(i, N):
                i += 1
                if truck >= objs[j]:
                    ans += objs[j]
                    break

    print('#{} {}'.format(t, ans))
