alpha_1 = input().lower()
alpha_2 = input().lower()

if alpha_1 < alpha_2:
    print("-1")
elif alpha_2 < alpha_1:
    print("1")
elif alpha_1 == alpha_2:
    print("0")


