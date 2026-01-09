class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_cons{};

        for (size_t i = 0; i < nums.size(); ++i)
        {
            int cur_cons{};
            size_t j = i;
            if (nums[i] == 1)
            {
                while (j < nums.size() && nums[j] == 1)
                {
                    ++cur_cons;
                    ++j;
                }
            }
            if (cur_cons > max_cons)
            {
                max_cons = cur_cons;
            }
            if (j == nums.size())
            {
                return max_cons;
            }
        }

        return max_cons;
    }
};