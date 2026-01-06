class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int, int> counter;

        for (auto& i : nums) {
            if (counter.contains(i)) {
                counter[i] += 1;
            } else {
                counter[i] = 1;
            }
            if (counter[i] >= (nums.size() / 2) + 1) return i;
        }
        return 0;

        
    }
};