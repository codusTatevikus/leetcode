class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = 0
        result = []
        for i in range(0, len(nums)):
            for j in range (0, len(nums)):
                if i != j and nums[i] > nums[j]:
                    answer += 1
            result.append(answer)
            answer = 0
        return result