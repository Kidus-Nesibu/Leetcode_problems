num_input = int(input())
num = list(map(int, input().split()))
result = []

for i in range(num_input):

    result.append(abs(num[i]))
    result.sort()
print(result[0])