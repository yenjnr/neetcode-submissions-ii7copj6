class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> store;
        vector<vector<int>>  freq(nums.size() + 1);

        for (int i : nums) {
            store[i] = 1 + store[i];
        }
        for (const auto& entry : store) {
            freq[entry.second].push_back(entry.first);
        }
        
        vector<int> res;
        for (int i = freq.size() - 1; i > 0; --i) {
            for (int j : freq[i]) {
                res.push_back(j);
                if (res.size() == k){
                    return res;
                }
            }
        }
        return res;
    }
};
