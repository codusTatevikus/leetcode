class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> ans;

        for (size_t j = 0; j < words.size(); ++j)
        {
            for (size_t i = 0; i < words[j].size(); ++i)
            {
                if (words[j][i] == x)
                {
                    ans.push_back(j);
                    break;
                }
            }
        }

        return ans;
    }
};