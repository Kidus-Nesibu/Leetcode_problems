num_input = int(input())

for i in range(num_input):
    count_A = 0
    count_B = 0
    word = input()

    for j in range(5):
        if word[j] == 'A':
            count_A += 1
        elif word[j] == 'B':
            count_B += 1

    if count_A > count_B:
        print('A')
    elif count_B > count_A:
        print('B')