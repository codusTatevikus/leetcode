class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int answer{};

        for (size_t i = 0; i < nums.size(); ++i)
        {
            int digits{};
            while (nums[i])
            {
                ++digits;
                nums[i] /= 10;
            }
            if (digits % 2 == 0)
            {
                ++answer;
            }
        }

        return answer;
    }
};