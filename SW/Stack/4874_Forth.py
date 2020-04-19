import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Stack
# 발상 : 후위 표기법
# 변형 : Forth 언어(후위 표기법 사용)를 연산하라
# 조합 :

T = int(input())
for t in range(1, T+1):
    element = input().split()
    stack = []
    ans = ''
    for x in element:
        if x == '.':
            if len(stack) != 1:  # 마지막 스택에 원소 없거나 2개 이상
                ans = 'error'
                break
            else:
                ans = stack[0]
        elif x in ['+', '-', '*', '/']:
            if not stack:
                ans = 'error'
                break
            end = int(stack.pop())
            if not stack:
                ans = 'error'
                break
            start = int(stack.pop())
            if x == '+':
                stack.append(start + end)
            elif x == '-':
                stack.append(start - end)
            elif x == '*':
                stack.append(start * end)
            elif x == '/':
                stack.append(start // end)
        else:
            stack.append(int(x))
    print('#{} {}'.format(t, ans))
