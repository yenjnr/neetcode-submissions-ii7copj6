class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max1,max2,max3=0,0,0
        for i,j,k in triplets:
            if i>target[0] or j>target[1] or k>target[2]:
                continue
            max1=max(max1,i)
            max2=max(max2,j)
            max3=max(max3,k)

        if max1!= target[0] or max2!=target[1] or max3!=target[2]:
            return False

        return True
