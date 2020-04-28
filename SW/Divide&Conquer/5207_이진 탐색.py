import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Binary Search
# 발상 : 이진 탐색 -> 탐색 범위 반으로 좁히기
# 변형 : 존재하는 원소에 대해 탐색 과정에서 양쪽 구간을 번갈아 선택하게 되는 숫자의 개수
# 조합 : Divide & Conquer

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))  # 정렬된 상태로 저장
    B = list(map(int, input().split()))
    cnt = 0

    for x in B:
        flag, l, r = 0, 0, N-1
        while l <= r:
            m = (l + r) // 2
            if A[m] == x:
                cnt += 1
                break
            elif A[m] < x:
                if flag == 1:
                    break
                l = m+1
                flag = 1
            elif A[m] > x:
                if flag == -1:
                    break
                r = m-1
                flag = -1

    print('#{} {}'.format(t, cnt))
