import sys
sys.stdin = open('sample_input.txt', 'r')


def bubble_sort(arr_len, arr):
    for i in range(arr_len-1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


T = int(input())
for t in range(T):
    n = int(input())

    # 1 : Python 내장함수 sorted O(nlogn)
    # a = sorted(map(int, input().split(' ')))
    # print('#{} {}'.format(t+1, a[n-1]-a[0]))

    # 2 : bubble sort O(n^2)
    a = list(map(int, input().split(' ')))
    res = bubble_sort(n, a)
    print('#{} {}'.format(t + 1, res[n - 1] - res[0]))
