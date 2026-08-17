class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryOut = True

        addOne = list(digits)

        for i in range(len(addOne) - 1, -1, -1):
            if addOne[i] == 9:
                addOne[i] = 0
            else:
                addOne[i] += 1
                carryOut = False
                break

        if carryOut:
            addOne.insert(0, 1)

        return addOne