class Solution {
public:
    string defangIPaddr(string address) {
        string ans{ address[0] };

        for (size_t i = 0; i < address.size(); i += 2)
        {
            if (address[i] == '.')
            {
                ans += "[.]";
            }
            else
            {
                ans += address[i];
            }
        }

        return ans;
    }
};