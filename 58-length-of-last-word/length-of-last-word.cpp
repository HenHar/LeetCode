class Solution {
public:
    int lengthOfLastWord(string s) {
        int len_last_word = s.length();
        bool count = false;
        string space = " ";
        for (int i = s.length()-1; i >= 0; i--) {
            if (!count && s.substr(i, 1).compare(space) != 0) {
                count = true;
                len_last_word = 0;
            }
            if (count && s.substr(i, 1).compare(space) == 0)
                return len_last_word;
            if (count)
                len_last_word++;
        }
        return len_last_word;
    }
};