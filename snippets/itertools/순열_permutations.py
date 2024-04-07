from itertools import permutations as iter_permu
arr = [1, 2, 3, 4]
visited = [False] * len(arr)

all_permutations = []
def permutations(n, current):
    if len(current) == n:
        all_permutations.append(current)
        return
    for i in range(len(arr)):
        if not visited[i]:
            # 백트래킹
            visited[i] = True
            permutations(n, current + [arr[i]])
            visited[i] = False

print('=' * 10, "정의한 permutations의 결과", '=' * 10)
permutations(2, [])
print(all_permutations)
print('=' * 10, "itertools permutations의 결과", '=' * 10)
print(list(iter_permu(arr, 2)))