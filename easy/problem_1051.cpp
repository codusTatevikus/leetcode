class Solution {
public:
    int heightChecker(vector<int>& heights) {
        int count{};

        vector<int> expected = heights;
        sort(expected.begin(), expected.end());

        for (size_t i = 0; i < heights.size(); ++i)
        {
            if (expected[i] != heights[i])
            {
                ++count;
            }
        }

        return count;
    }
};