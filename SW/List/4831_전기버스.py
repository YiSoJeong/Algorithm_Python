import sys
sys.stdin = open('sample_input.txt', 'r')
# 분류 : Greedy Algorithm
# 발상 : 충전이 가능하면 충전 but 불가능 하더라도 직전 충전소에 들리면 가능할 수도 -> Greedy?
# 조합 : 구현 -> 버스 이동시 조건 맞추기

T = int(input())
for t in range(1, T+1):
    k, n, m = map(int, input().split())
    num = list(map(int, input().split()))

    arr = [False] * (n+1)
    for i in range(n+1):
        if i in num:
            arr[i] = True

    cnt = move = 0
    while move < n:  # n제외 : 이미 도착
        if arr[move]:
            cnt += 1
        elif move > 0:  # 0제외 : 처음은 충전 되어있음
            near = 0
            for x in num:
                if move-k < x < move:
                    if x > near:
                        near = x
            if near > 0:
                cnt += 1
                move = near
            else:  # 충전 불가
                cnt = 0
                break
        move += k

    print('#{} {}'.format(t, cnt))
