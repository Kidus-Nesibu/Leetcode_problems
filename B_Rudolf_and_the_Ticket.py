num_input = int(input())

for i in range(num_input):

    k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))

    count_l = 0
    count_z = 0
    bigger = max(k)

    for x in range(len(l)):

        if l[x] < bigger and l[x] >= 0:
            count_l += 1
        else:
            continue
    
    for z in range(len(r)):
        if  r[z] < bigger and r[z] >= 0:
            count_z += 1
        else:
            continue
    
    result = count_l * count_z
    print(result)
