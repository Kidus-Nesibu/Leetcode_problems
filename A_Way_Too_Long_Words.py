word_count = int(input())

for i in range(word_count):
    
    word = input().strip()
    length = len(word)

    if length > 10:
        word = word[0] + str(length - 2) + word[-1]

    print(word)
        