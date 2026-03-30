class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexList = dict()

        for i, j in enumerate(nums):
            needed = target - j
            if needed in indexList:
                return [indexList[needed], i]
            indexList[j] = i