class Solution {
public:
    int numberOfSteps(int num) {
        int count{};

        while (num)
        {
            if ((num & 1) == 0)
            {
                num >>= 1;
            }
            else
            {
                --num;
            }
            ++count;
        }
        return count;
    }
};