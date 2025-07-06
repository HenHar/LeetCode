#include <ranges> 

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> seen_nums;

        for (auto [idx, num] : std::views::enumerate(nums)) {
            if (seen_nums.contains(num)) 
                return std::vector<int>{seen_nums[num], static_cast<int>(idx)};
            seen_nums[target - num] = idx;
        }
        return {};
    }

        vector<int> twoSum2(vector<int>& nums, int target) {
        for (int i1 = 0; i1 < nums.size(); i1++) {
            for (int i2 = i1+1; i2 < nums.size(); i2++) { 
                if (nums[i1] + nums[i2] == target)
                    return vector<int>{i1, i2};
            }
        }
        return vector<int>{};
    }
};