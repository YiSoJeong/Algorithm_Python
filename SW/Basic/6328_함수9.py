arr = input().split(', ')


def longest_str(li):
    ans = li[0]
    for x in li:
        if len(ans) < len(x):
            ans = x
    print(x)


longest_str(arr)