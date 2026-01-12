class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count{};

        for (size_t i = 0; i < nums.size(); ++i)
        {
            if (nums[i] == val)
            {
                ++count;
                nums[i] = 51;
            }
        }
        sort(nums.begin(), nums.end());

        return nums.size() - count;
    }
};

#2

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count{};

        for (size_t i = 0; i < nums.size(); ++i)
        {
            if (nums[i] != val)
            {
                nums[count] = nums[i];
                ++count;
            }
        }

        return count;
    }
};