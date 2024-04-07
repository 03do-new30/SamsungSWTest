from itertools import combinations as iter_combinations
arr = [1, 2, 3, 4]
all_combinations = []
def combinations(n, current, index):
    if len(current) == n:
        all_combinations.append(current)
        return
    for i in range(index, len(arr)):
        combinations(n, current + [arr[i]], i + 1)

print('=' * 10, "정의한 combinations 결과", '=' * 10)
combinations(2, [], 0)
print(all_combinations)
print('=' * 10, "itertools combinations 결과", '=' * 10)
print(list(iter_combinations(arr, 2)))