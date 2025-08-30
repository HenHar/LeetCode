#include <ranges> 

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int i = 0, j = 1, k = 2;
        int num_items = nums.size();
        sort(nums.begin(), nums.end());
        


        std::map<int, int> seen_nums;
        for (int i = 0; i < num_items; i++) {
            seen_nums[nums[i]] = i;
        }

        std::vector<std::vector<int>> result;
        for (int i = 0; i < num_items; i++) {
            if (nums[i] > 0) {
                break;
            }
            for (int j = i + 1; j < num_items; j++) {
                int required = -1 * (nums[i] + nums[j]);
                if (seen_nums.contains(required) && seen_nums[required] > j) {
                    result.push_back({nums[i], nums[j], required});
                }
                j = seen_nums[nums[j]];
            }
            i = seen_nums[nums[i]];
        }
    

        return result;
    }
};