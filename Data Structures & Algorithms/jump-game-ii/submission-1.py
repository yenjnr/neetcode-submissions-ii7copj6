class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n):
            # Have we reached the current_end?
            if i > current_end:
                jumps += 1
                current_end = farthest

            # Have we found new maximum?
            if i + nums[i] > farthest:
                farthest = i + nums[i]
        
        return jumps