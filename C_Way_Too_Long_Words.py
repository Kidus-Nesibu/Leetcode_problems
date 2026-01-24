num_input = int(input())

for i in range(num_input):
    word = input()
    if len(word) > 10:
        num = len(word) - 2
        print(word[0] + str(num) + word[-1])
    else:
        print(word)