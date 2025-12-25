import math
def theatre_square(n, m, a) -> int:

    height = math.ceil(n/a)
    width = math.ceil(m/a)

    result = width * height

    return result 

print(theatre_square(6, 6, 4))


