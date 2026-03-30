class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sqn = defaultdict(int)
        res = 0

        for i in nums:
            if not sqn[i]:
                sqn[i] = sqn[i - 1] + sqn[i + 1] + 1
                sqn[i - sqn[i - 1]] = sqn[i]
                sqn[i + sqn[i + 1]] = sqn[i]
                res = max(res, sqn[i])     
        return res