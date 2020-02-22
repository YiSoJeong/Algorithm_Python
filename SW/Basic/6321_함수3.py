# n 까지의 자연수 중 소수 구하기, 판별하

n = int(input())


# 1 : 자기 자신보다 작은 수 중에 나누어 떨어지는 수가 없는지 판별
def prime_bad(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# 2 : 제곱근을 활용해 반복 수 감소 + 트릭 -> 최적화
def prime_good(x):
    # 10 미만
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n < 9:
        return True
    # 10 이상
    k, root = 5, x ** 0.5
    while k <= root:
        if x % k == 0 or x % (k+2) == 0:
            return False
        k += 6
    return True


# 3 : 에라토스테네스의 체 -> 일정한 범위가 주어졌을 경우 사용가능
def find_prime(x):
    nums = [False, False] + [True] * (x - 1)
    for k in range(2, round(x ** 0.5) + 1):
        if nums[k]:
            nums[2*k::k] = [False] * ((x - k) // k)
    return [x for x in range(x+1) if nums[x]]


if prime_good(n):
    print('소수입니다.')
else:
    print('소수가 아닙니다.')