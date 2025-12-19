class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        for (size_t i = 1; i < nums.size(); ++i)
        {
            for (size_t j = i - 1; j < i; ++j)
            {
                nums[i] += nums[j];
            }
        }
        return nums;
    }
};