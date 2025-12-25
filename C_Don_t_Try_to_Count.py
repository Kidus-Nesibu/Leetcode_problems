t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    x = input().strip()
    s = input().strip()

    ops = 0
    found = False

    while len(x) <= 200:
        print(ops)