class Solution {
public:
    int differenceOfSums(int n, int m) {
        int nums1{}, nums2{};

        while (n) {
            if (n % m == 0) {
                nums2 += n;
            }
            else
            {
                nums1 += n;
            }
            --n;
        }

        return nums1 - nums2;
    }
};