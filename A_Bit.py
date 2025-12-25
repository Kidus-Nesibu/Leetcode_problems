num_input = int(input())

x = 0
for i in range(num_input):

    statment = input()

    if "++" in statment:
        x += 1
    elif "--" in statment:
        x -= 1
print(x)