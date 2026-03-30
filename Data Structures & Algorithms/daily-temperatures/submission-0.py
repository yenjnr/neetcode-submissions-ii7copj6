class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        dayList = [0] * length
        
        for i in range(length - 2, -1, -1):
            j = i + 1
            while j < length and temperatures[j] <= temperatures[i]:
                if dayList[j] == 0:
                    j = length
                    break
                j += dayList[j]
            if j < length:
                dayList[i] = j - i
        return dayList