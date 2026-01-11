class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        size_t n = arr.size();
        for (size_t i = 0; i < n; ++i)
        {
            if (arr[i] == 0)
            {
                arr.insert(arr.begin() + i, 0);
                ++i;
            }
        }
        arr.resize(n);
    }
};