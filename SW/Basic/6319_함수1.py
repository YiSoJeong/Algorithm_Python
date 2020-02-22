a = input()


def reverse_str(s):
    return s[::-1]


print(reverse_str(a))
if a == reverse_str(a):
    print('입력하신 단어는 회문(Palindrome)입니다.')