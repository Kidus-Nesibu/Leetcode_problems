class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        num_count = {}

        for i in nums:
            if i not in num_count:
                num_count[i] = 1
            else:
                num_count[i] += 1

        for keys in num_count:
            if num_count[keys] >  1:
                return keys
            else:
                continue
