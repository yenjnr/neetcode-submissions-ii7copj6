class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> checked;
        int n = nums.size();
        
        for (int i = 0; i < n; i++) {
            int needed = target - nums[i];
            if (checked.find(needed) != checked.end()){
                return {checked[needed], i};
            }
            
            checked.insert({nums[i], i});
        }
        return {};
    }
};
