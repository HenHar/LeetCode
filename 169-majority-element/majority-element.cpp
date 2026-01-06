class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int, int> counter;

        for (auto& i : nums) {
            if (counter.contains(i)) counter[i] += 1;
            else counter[i] = 1;    
        }

        int min_size = nums.size() / 2;
        for (auto& item : counter) {
            if (item.second > min_size) return item.first;
        }
        return 0;

        
    }
};