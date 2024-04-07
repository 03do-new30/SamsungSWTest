from itertools import product as iter_product

arr = [1, 2, 3, 4]
all_products = []

def product(n, current):
    if len(current) == n:
        all_products.append(current)
        return
    for i in range(len(arr)):
        product(n, current + [arr[i]])


print('=' * 10, "정의한 product의 결과", '=' * 10)
product(2, [])
print(all_products)
print('=' * 10, "itertools product의 결과", '=' * 10)
print(list(iter_product(arr, repeat=2)))
