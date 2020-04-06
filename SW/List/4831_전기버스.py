import sys
sys.stdin = open('../String/sample_input.txt', 'r')
# 분류 : Greedy Algorithm
# 발상 : 충전이 가능하면 충전 but 불가능 하더라도 직전 충전소에 들리면 가능할 수도 -> Greedy?
# 조합 : 구현 -> 버스 이동시 조건 맞추기

# sol1
# T = int(input())
# for t in range(1, T+1):
#     k, n, m = map(int, input().split())
#     num = list(map(int, input().split()))
#
#     arr = [False] * (n+1)
#     for i in range(n+1):
#         if i in num:
#             arr[i] = True
#
#     cnt = move = 0
#     while move < n:  # n제외 : 이미 도착
#         if arr[move]:
#             cnt += 1
#         elif move > 0:  # 0제외 : 처음은 충전 되어있음
#             near = 0
#             for x in num:
#                 if move-k < x < move:
#                     if x > near:
#                         near = x
#             if near > 0:
#                 cnt += 1
#                 move = near
#             else:  # 충전 불가
#                 cnt = 0
#                 break
#         move += k
#
#     print('#{} {}'.format(t, cnt))

# sol2
T = int(input())
for t in range(1, T+1):
    k, n, m = map(int, input().split())
    num = list(map(int, input().split()))
    num.append(n)  # 도착지 포함
    cur = cnt = 0
    charge = k
    for x in num:
        # 다음 정류장까지 갈 수 있을 때
        if charge + cur >= x:
            charge -= x-cur
            cur = x
        # 없을 때 -> 충전하면?
        else:
            charge = k
            cnt += 1
            if charge + cur >= x:
                charge -= x-cur
                cur = x
            else:
                cnt = 0
                break

    print('#{} {}'.format(t, cnt))
