class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> sqn;
        int res = 0;

        for (int i : nums) {
            if (!sqn[i]) {
                sqn[i] = sqn[i - 1] + sqn[i + 1] + 1;
                sqn[i - sqn[i - 1]] = sqn[i];
                sqn[i + sqn[i + 1]] = sqn[i];
                res = max(res, sqn[i]);
            }
        }
        return res;
    }
};
