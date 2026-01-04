class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int wealth{};

        for (size_t i = 0; i < accounts.size(); ++i)
        {
            int wealthSum{};
            for (size_t j = 0; j < accounts[i].size(); ++j)
            {
                wealthSum += accounts[i][j];
            }
            wealth = max(wealth, wealthSum);
        }
        return wealth;
    }
};