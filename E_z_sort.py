n = int(input())
a = list(map(int, input().split()))

a.sort()

result = [0] * n
l, r = 0, n-1

for i in range(n):
    if i % 2 == 0:
        result[i] = a[l]
        l += 1
    else:
        result[i] = a[r]
        r -= 1

print(*result)