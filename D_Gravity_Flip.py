num_input = int(input())

nums = list(map(int, input().split()))
nums.sort()
print(*nums)