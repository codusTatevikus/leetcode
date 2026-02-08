class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer = 0
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] == nums[j]):
                    answer += 1

        return answer