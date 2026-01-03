class Solution {
public:
    string truncateSentence(string s, int k) {
        int count{};

        for (size_t i = 0; i < s.size(); ++i)
        {
            if (s[i] == ' ')
            {
                ++count;
            }
            if (count == k)
            {
                s.resize(i);
                break;
            }
        }

        return s;
    }
};