n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
# print("시험장:", a)
# print("총감독관:", b, "부감독관:", c)
# 각 시험장에 총감독관은 1명만, 부감독관은 여러명

# 각 시험장에서 총감독관이 감독할 수 있는 학생 수를 빼준다
for i in range(n):
    a[i] -= b
answer = n

# 부감독관이 감독할 수 있는 학생 수를 구한다
for i in range(n):
    if a[i] > 0:
        if a[i] % c == 0:
            answer += a[i] // c
        else:
            answer += a[i] // c + 1
print(answer)