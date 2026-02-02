class Solution:
    def maxDistinct(self, s: str) -> int:
        unique = set(s)
        return len(unique)