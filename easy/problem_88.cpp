class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int left{};
        int right{};
        vector<int> p;

        while (left < m && right < n)
        {
            if (nums1[left] < nums2[right])
            {
                p.push_back(nums1[left]);
                ++left;
            }
            else
            {
                p.push_back(nums2[right]);
                ++right;
            }
        }

        while (left < m)
        {
            p.push_back(nums1[left]);
            ++left;
        }

        while (right < n)
        {
            p.push_back(nums2[right]);
            ++right;
        }

        nums1 = p;
    }
};