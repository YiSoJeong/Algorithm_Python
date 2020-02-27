a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}
uni_dict = {}

a_keys = a.keys()
b_keys = b.keys()
dup = a_keys & b_keys
# print(dup) # {'아메리카노', '카페모카'}

for k, v in a.items():
    if k not in dup:
        uni_dict[k] = v
    else:
        if a[k] > b[k]:
            uni_dict[k] = v
        else:
            uni_dict[k] = b[k]

for k, v in b.items():
    if k not in dup:
        uni_dict[k] = v

print({(k, v) for k, v in uni_dict.items() if v >= 3000})
