from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        previous = 0
        next = 1

        while next < len(nums):
            if nums[next] != nums[previous]:
                previous += 1
                nums[previous] = nums[next]
            next += 1

        return previous + 1
