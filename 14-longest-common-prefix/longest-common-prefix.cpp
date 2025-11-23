class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        string word = strs[0];

        int prefix_end = 0;
        while(true) {
            prefix = word.substr(0,prefix_end);
            for (auto& word : strs) {
                if (prefix_end > word.size())
                    return prefix.substr(0, prefix_end-1);
                if (word.substr(0,prefix_end) != prefix)
                    return prefix.substr(0, prefix_end-1);
            }
            prefix_end++;
        }
        return prefix;
    }
};