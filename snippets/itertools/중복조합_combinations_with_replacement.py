from itertools import combinations_with_replacement as iter_cwr

arr = [1, 2, 3, 4]
all_results = []
# 순서 X, 중복 O
# 조합과 동일하게 현재 인덱스를 의미하는 매개변수가 추가됨
# 중복 가능하므로 재귀 돌릴 때 현재 인덱스 +1이 아닌 현재 인덱스 값을 그대로 넘긴다
def combinations_with_replacement(n, current, index):
    if len(current) == n:
        all_results.append(current)
        return
    for i in range(index, len(arr)):
        combinations_with_replacement(n, current + [arr[i]], i)


print('=' * 10, "정의한 combinations_with_replacement의 결과", '=' * 10)
combinations_with_replacement(2, [], 0)
print(all_results)
print('=' * 10, "itertools combinations_with_replacement의 결과", '=' * 10)
print(list(iter_cwr(arr, 2)))