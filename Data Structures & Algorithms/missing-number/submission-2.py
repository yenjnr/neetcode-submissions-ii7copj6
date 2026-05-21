class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = sum(i+1 for i in range(0, len(nums)))

        actual_sum = sum(i for i in nums)

        return expected_sum - actual_sum
        