class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxList = []

        for l in range(len(nums) - k + 1):
            maxElement = float('-inf')
            r = l + k
            for i in range(l, r):
                maxElement = max(maxElement, nums[i])
            maxList.append(maxElement)
        return maxList