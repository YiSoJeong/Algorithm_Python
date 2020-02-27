products = {"TV": 2000000, "냉장고": 1500000, "책상": 350000, "노트북": 1200000, "가스레인지": 200000, "세탁기": 1000000}
# lambda 매개변수: 반환값
sorted_products = {k: v for k, v in sorted(products.items(), key=lambda item: item[1], reverse=True)}

for key, val in sorted_products.items():
    print('{}: {}'.format(key, val))
