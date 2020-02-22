a = input()


def reverse_str(s):
    ret = ''
    for i in range(len(s)-1, -1, -1):
        ret += s[i]
    return ret


print(reverse_str(a))
if a == reverse_str(a):
    print('입력하신 단어는 회문(Palindrome)입니다.')