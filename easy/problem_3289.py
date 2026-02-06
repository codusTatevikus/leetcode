class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            if nums[i] in nums[i + 1:]:
                result.append(nums[i])
        return result