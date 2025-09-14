class Solution {
public:
    int lengthOfLastWord(string s) {
        int len_last_word = 0;
        bool count = false;
        for (int i = s.length()-1; i >= 0; i--) {
            if (s[i] != ' ') {
                count = true;
                len_last_word++;
            }
            else if (count)
                return len_last_word;
        }
        return len_last_word;
    }
};