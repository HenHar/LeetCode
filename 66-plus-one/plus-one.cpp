class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int transfer = 1;
        for (int i = digits.size()-1; i >= 0; i--) {
            if (transfer != 0) {
                int sum = digits[i] + transfer;
                transfer = 0;
                digits[i] = sum;
                if (sum > 9) {
                    digits[i] = 0;
                    transfer = 1;
                }
            }
        }
        if (transfer != 0)
            digits.insert(digits.begin(), transfer);
        return digits;
    }
};