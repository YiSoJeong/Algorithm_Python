import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : 진수 변환
# 발상 : 10진수 -> 2진수
# 변형 : 소수 부분
# 조합 :
# https://blog.naver.com/PostView.nhn?blogId=okkam76&logNo=221365971022&parentCategoryNo=&categoryNo=7&viewDate=&isShowPopularPosts=false&from=postView

T = int(input())
for t in range(1, T+1):
    num = float(input())
    res = ''
    while num:
        num *= 2
        bit = int(num)
        if len(res) > 12:
            res = 'overflow'
            break
        res += str(bit)
        num -= bit
    print('#{} {}'.format(t, res))
