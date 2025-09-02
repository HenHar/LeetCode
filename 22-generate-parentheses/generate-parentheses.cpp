class Solution {
public:
    vector<string> generateParenthesis(int n) {
        map<int, vector<string>> parenthesis;
        parenthesis[0] = {""};
        parenthesis[1] = {"()"};

        for (int i = 2; i <= n; i++) {
            set<string> combinations_current_index;
            for (const auto& item : parenthesis[i - 1]) {
                for (int i2 = 0; i2 < item.size(); i2++) {
                    string combination = item.substr(0,i2) + "()" + item.substr(i2, item.size());
                    combinations_current_index.insert(combination);
                }
            }
            parenthesis[i] = std::vector<string>(combinations_current_index.begin(), combinations_current_index.end());
;
        }
        return parenthesis[n];
    }
};