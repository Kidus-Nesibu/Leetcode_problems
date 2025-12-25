num_input = int(input())

vote_count = 0
for i in range(num_input):

    vote = list(map(int, input().split()))

    if sum(vote) >= 2:
        vote_count += 1
print(vote_count)