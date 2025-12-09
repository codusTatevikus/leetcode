class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int count{};

        for (size_t i = 0; i < nums.size(); ++i)
        {
            if (nums[i] % 3 != 0)
            {
                ++count;
            }
        }

        return count;
    }
};