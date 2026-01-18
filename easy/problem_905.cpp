class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int j{};

        for (size_t i = 0; i < nums.size(); ++i)
        {
            if (nums[i] % 2 == 0)
            {
                swap(nums[j], nums[i]);
                ++j;
            }
        }

        return nums;
    }
};