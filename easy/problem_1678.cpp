class Solution {
public:
    string interpret(string command) {
        string result;

        for (size_t i = 0; i < command.size(); ++i)
        {
            if (command[i] == 'G')
            {
                result += 'G';
            }
            else if (command[i] == '(' && command[i + 1] == 'a')
            {
                result += "al";
                i += 3;
            }
            else
            {
                result += 'o';
                i += 1;
            }
        }
        return result;
    }
};