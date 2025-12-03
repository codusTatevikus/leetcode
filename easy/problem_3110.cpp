class Solution {
public:
    int scoreOfString(string s) {
        int answer{};

        for (size_t i = 1; i < s.size(); ++i)
        {
            answer += abs(s[i - 1] - s[i]);
        }

        return answer;
    }
};