string = input()
alphabet = dict()

for x in string:
    if x in alphabet:
        alphabet[x] += 1
    else:
        alphabet[x] = 1

for k, v in alphabet.items():
    print('{},{}'.format(k, v))
