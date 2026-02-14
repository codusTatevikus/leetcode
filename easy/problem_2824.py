class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        answer = 0
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    answer += 1
        return answer