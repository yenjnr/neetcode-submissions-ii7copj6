class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> output;
        int i = 0;
        while (i < intervals.size()) {
            int start = intervals[i][0], end = intervals[i][1];
            while (i + 1 < intervals.size() && end >= intervals[i + 1][0]) {
                end = max(end, intervals[i + 1][1]);
                i++;
            }
            output.push_back({start, end});
            i++;
        }
        return output;
    }
};
