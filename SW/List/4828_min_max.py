import sys
sys.stdin = open('sample_input.txt', 'r')

MAX_NUM = 1000000


def bubble_sort(arr_len, arr):
    for i in range(arr_len-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def counting_sort(arr_len, arr):
    sorted_arr = [0]*arr_len
    count = [0]*(MAX_NUM+1)

    for x in arr:
        count[x] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i in range(arr_len):
        sorted_arr[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1

    return sorted_arr


T = int(input())
for t in range(T):
    n = int(input())

    # 1 : Python 내장함수 sorted O(nlogn)
    # a = sorted(map(int, input().split()))
    # print('#{} {}'.format(t+1, a[n-1]-a[0]))

    # 2 : bubble sort O(n^2)
    # a = list(map(int, input().split()))
    # res = bubble_sort(n, a)
    # print('#{} {}'.format(t + 1, res[n - 1] - res[0]))

    # 3 : counting sort O(n + k(최대 정수))
    a = list(map(int, input().split()))
    res = counting_sort(n, a)
    print('#{} {}'.format(t + 1, res[n - 1] - res[0]))
