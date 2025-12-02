class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int numsSum{};

        for (auto& num : nums)
        {
            numsSum += num;
        }

        return numsSum % k;
    }
};