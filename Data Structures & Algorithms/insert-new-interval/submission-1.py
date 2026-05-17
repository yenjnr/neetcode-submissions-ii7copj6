class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]
        if not newInterval:
            return [intervals]

        res = []
        i = 0
        flag = True
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
            
            elif interval[0]> newInterval[1]:
                if flag:
                    res.append(newInterval)
                    flag = False
                res.append(interval)
            else:
                newInterval[0] = min(interval[0],newInterval[0])
                newInterval[1] = max(interval[1],newInterval[1])
        
        if flag:
            res.append(newInterval)
        
        return res
        