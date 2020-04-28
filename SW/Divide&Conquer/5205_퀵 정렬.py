import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Divide & Conquer
# 발상 : 퀵 정렬 -> 분할정복
# 변형 : 퀵 정렬한 배열의 가운데 값
# 조합 : 재귀


def partition_lomuto(l, r):
    global arr
    x = arr[r]
    L = l-1
    for R in range(l, r):
        if arr[R] <= x:
            L += 1
            arr[L], arr[R] = arr[R], arr[L]
    arr[L+1], arr[r] = arr[r], arr[L+1]
    return L+1


def partition_hoare(l, r):
    global arr
    pivot = (l + r) // 2
    while l < r:
        while arr[l] < arr[pivot] and l < r:
            l += 1
        while arr[r] >= arr[pivot] and l < r:
            r -= 1
        if l < r:
            if l == pivot:
                pivot = r
            arr[l], arr[r] = arr[r], arr[l]
    arr[r], arr[pivot] = arr[pivot], arr[r]
    return r


# 2 / 10 (제한시간 초과)
def quick_sort(l, r):
    if l < r:
        p = partition_hoare(l, r)
        # p = partition_lomuto(l, r)
        quick_sort(1, p-1)
        quick_sort(p+1, r)


# 9 / 10 Runtime Error -> 느린가..?
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     lesser_arr, equal_arr, greater_arr = [], [], []
#     for num in arr:
#         if num < pivot:
#             lesser_arr.append(num)
#         elif num > pivot:
#             greater_arr.append(num)
#         else:
#             equal_arr.append(num)
#     return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


# Python스럽게
# def quicksort(arr):
#     if not arr:
#         return []
#
#     pivots = [x for x in arr if x == arr[0]]
#     lesser = quicksort([x for x in arr if x < arr[0]])
#     greater = quicksort([x for x in arr if x > arr[0]])
#
#     return lesser + pivots + greater


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # sort_arr = quicksort(arr)
    quick_sort(0, N-1)
    # print(sorted(arr)[N//2]) # 내장함수
    print('#{} {}'.format(t, arr[N//2]))
