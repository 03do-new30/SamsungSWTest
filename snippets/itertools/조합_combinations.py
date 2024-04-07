from itertools import combinations as iter_combinations
arr = [1, 2, 3, 4]
all_combinations = []

# 현재 인덱스를 의미하는 매개변수가 추가됨
# 순서가 상관 없고 중복불가이기 때문에 현재 인덱스보다 작거나 같은 인덱스는 볼 필요가 없음
# 재귀 돌릴 때 현재 인덱스 + 1 값을 넘긴다
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