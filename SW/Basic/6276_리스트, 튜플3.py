dan_list = []

for dan in range(2, 10):
    li = [dan * i for i in range(1, 10) if (dan * i) % 3 != 0 if (dan * i) % 7 != 0]
    dan_list.append(li)

print(dan_list)
