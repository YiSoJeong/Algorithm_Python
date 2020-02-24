string = 'abcdef'
ret = {}

for idx, val in enumerate(string):
    ret[val] = idx

for k in ret.keys():
    print('{}: {}'.format(k, ret[k]))
