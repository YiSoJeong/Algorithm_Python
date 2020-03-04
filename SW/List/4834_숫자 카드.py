import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Brute force
# 발상 : 입력받은 모든 수의 정보를 알아야 하니까
# 변형 : 입력받은 수를 idx에 따라 추가
# 조합 : 구현

T = int(input())
for t in range(1, T+1):
    arr = [0] * 10
    n = input()
    nums = input()
    for x in nums:
        arr[int(x)] += 1
    max_num = 0
    max_idx = 0
    for i in range(len(arr)):
        if arr[i] >= max_num:
            max_idx = i
            max_num = arr[i]
    print('#{} {} {}'.format(t, max_idx, max_num))
