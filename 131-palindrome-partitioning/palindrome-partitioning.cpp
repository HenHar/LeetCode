#include <string>
#include <vector>

class Solution {
public:
    int len_word;
    vector<vector<string>> result;
    string word;


    void backtrack(int i, vector<string> current) {
        if (i == len_word) {
            if (is_valid(current.back()))
                result.push_back(current);
            return;
        }

        // add character as new string
        vector<string> new_string_branch = current;
        if (is_valid(new_string_branch.back())) {
            new_string_branch.push_back(string(1, word[i]));
            backtrack(i + 1, new_string_branch);
        }
        // add char to current string      
        vector<string> append_branch = current;
        append_branch.back() += word[i];
        backtrack(i + 1, append_branch);
    
    }

    bool is_valid(const std::string& str) {
        int left = 0;
        int right = str.length() - 1;

        while (left < right) {
            if (str[left] != str[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    vector<vector<string>> partition(string s) {
        len_word = s.size();
        word = s;
        vector<string> current;
        current.push_back(string(1, word[0]));
        backtrack(1, current);
        return result;
    }
    
};