class Solution {
public:
    int romanToInt(string s) {
        int number = 0;
        int i = 0;
        while (i < s.length()) {
            if (mapping.find(s.substr(i, 2)) != mapping.end()) {
                number += mapping[s.substr(i, 2)];
                i=i+2;
            } else {
                number += mapping[s.substr(i, 1)];
                i++;
            }
        }
        return number;
    }



    std::map<std::string, int> mapping = {
        {"I", 1},
        {"V", 5},
        {"X", 10},
        {"L", 50},
        {"C", 100},
        {"D", 500},
        {"M", 1000},
        {"IV", 4},
        {"IX", 9},
        {"XL", 40},
        {"XC", 90},
        {"CD", 400},
        {"CM", 900}
    };



};