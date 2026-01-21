class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        multiple_n = [(n * 1), (n * 2)]
        multiple_2 = []

        num = 1
        product = 0
        while product < max(multiple_n):
            product = num * 2
            multiple_2.append(product)
            num += 1
        
        if multiple_n[0] in multiple_2:
            return multiple_n[0]
        elif multiple_n[1] in multiple_2:
            return multiple_n[1]