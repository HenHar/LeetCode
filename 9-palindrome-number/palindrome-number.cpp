class Solution {
public:
    bool isPalindrome(int x) {
        std::string num = std::to_string(x);
        int left = 0, right = num.length() - 1;
        while (left < right) {
            std::cout << left << num[left] << right << num[right];
            if (num[left] != num[right]) return false;
            left += 1;
            right -= 1;
        }
        return true;
    }
};