class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        length = len(nums)
        pre = [0] * length
        suf = [0] * length
        res = [0] * length

        pre[0] = suf[length - 1] = 1

        for i in range(1, length):
            pre[i] = nums[i - 1] * pre[i - 1]
        for i in range(length - 2, -1, -1):
            suf[i] = nums[i + 1] * suf[i + 1]
        for i in range(length):
            res[i] = pre[i] * suf[i]
        return res