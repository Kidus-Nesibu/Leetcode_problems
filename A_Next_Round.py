n, k = map(int, input().split())
score = list(map(int, input().split()))

count = 0
high_score = score[k - 1]

for i in range(n):

    if score[i] >= high_score and score[i] > 0:
        count += 1
print(count)