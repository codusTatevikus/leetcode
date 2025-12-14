class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int ans{};

        for (auto& operation : operations)
        {
            if (operation == "++X" || operation == "X++")
            {
                ++ans;
            }
            if (operation == "--X" || operation == "X--")
            {
                --ans;
            }
        }

        return ans;
    }
};