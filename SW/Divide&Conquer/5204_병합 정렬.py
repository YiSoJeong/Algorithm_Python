import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Divide & Conquer
# 발상 : 병합정렬 -> 분할정복
# 변형 : 병합 과정에서 왼쪽 마지막 원소 > 오른쪽 마지막 원소 인 경우의 수
# 조합 : 재귀


def merge_sort(a, l, r):
    global ans
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    left = merge_sort(left, l, mid-1)
    right = merge_sort(right, mid, r)

    if left[-1] > right[-1]:
        ans += 1
    return sorted(left+right)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    sort_arr = merge_sort(arr, 0, N-1)
    print('#{} {} {}'.format(t, sort_arr[N//2], ans))
