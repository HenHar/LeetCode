class Solution {
public:
    int strStr(string haystack, string needle) {
        int len_needle = needle.length();
        for (int i = 0; i < haystack.length(); i++) {
            if (needle == haystack.substr(i, len_needle))
                return i;
        }
        return -1;
    }
};