class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        result = s.split()
        length = len(result[-1])
        return length