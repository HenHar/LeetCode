class Solution {
public:
    void sortColors(vector<int>& nums) {
        map<int, int> counts = {{0, 0}, {1, 0}, {2, 0}};
        for(const int& num: nums) {
            counts[num] += 1;
        }

        int key = 0;
        int num_value = counts[key];
        for(int& num: nums) {
            while (num_value == 0) {
                key += 1;
                num_value = counts[key];
            }
            num = key;
            num_value--;
        }
    }
};