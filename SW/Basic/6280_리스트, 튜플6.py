n = int(input())
div = []

for i in range(1, round(n ** 0.5) + 1): # int(n ** 0.5 + 1.5)와 동일
    div.extend([i, n//i])

print(sorted(div))
