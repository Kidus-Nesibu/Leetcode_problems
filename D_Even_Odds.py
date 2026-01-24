nums = [int(item) for item in input().split()]
n = nums[0]
k = nums[1]

collection = []

for i in range(1, n+1):
    if i % 2 == 0:
        continue
    elif i % 2 > 0:
        collection.append(i)

for i in range(1, n+1):
    if i % 2 == 0:
        collection.append(i)
    elif i % 2 > 0:
        continue

print(collection[k-1])