num_chocolate = int(input())
chocolate = list(map(int, input().split()))
num_coupon = int(input())
coupon =list(map(int, input().split()))

chocolate.sort(reverse = True)
total = sum(chocolate)

for i in coupon:

    val = total - chocolate[i - 1]
    print(val)

