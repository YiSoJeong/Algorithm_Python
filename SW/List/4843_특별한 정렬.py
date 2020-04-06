import sys
sys.stdin = open('../String/sample_input.txt', 'r')

# 분류 : Selection Sort
# 발상 : n번째 큰/작은 수 -> 선택정렬
# 변형 : 큰/작은 번갈아 나옴
# 조합 : list 안의 원소 출력 by ' '.join

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(10):
        m = i
        if i % 2 == 0:  # 큰 수
            for j in range(i+1, n):
                if arr[m] < arr[j]:
                    m = j
        else:  # 작은 수
            for j in range(i+1, n):
                if arr[m] > arr[j]:
                    m = j
        arr[m], arr[i] = arr[i], arr[m]
    ret = ' '.join(map(str, arr[0:10]))
    print('#{} {}'.format(t, ret))
