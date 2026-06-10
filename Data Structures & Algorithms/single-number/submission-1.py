from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # '''initial soluion
        #    return Counter(nums).most_common()[::-1][0][0] #RTC O(c^3)
        # '''

        # #sorting solution RTC O(nlogn), SC O(1)
        # #return non repeting #
        # new_nums=sorted(nums) #RTC O(nlogn) this is SC O(n) not O(1). sorted() creates 
        # #a new list but list.sort() is SC O(1) sorts in place
        # l,r=0,1
        # if len(nums)<2:
        #     return nums[0]
        
        # while r<len(nums)-1: #RTC O(n)
        #     if new_nums[l]!=new_nums[r]:
        #         return new_nums[l]
            
        #     l+=2
        #     r+=2
        # return new_nums[l]


        # '''
        # Hash set approach: 
        # Idea: have a set to track the first occurence of any number
        # if a number is seen more than once, remove it
        # return the last number in the set

        # RTC: O(n)
        # SC: O(n)
        # '''

        # already_seen=set()

        # for num in nums: # RTC: O(n) 
        #     if num in already_seen:
        #         already_seen.remove(num) #RTC O(1)
        #     else:
        #         already_seen.add(num) # RTC O(1) SC O(n)
        
        # return list(already_seen)[0] #guaranteed to only have 
        # #1 element by the very definition of the problem therefore
        # #constant time complexity


        '''
        XOR Solution: 
        Key idea: given a^0=0 and a^a=0, we can XOR all integers begining with zero and the 
        single remaining final result will be the single occuring character as all double 
        characters will cancel out. We do not need to sort either as ^ is associative
        
        RTC: O(n)
        SC: O(1)
        '''
        
        res=0

        for num in nums:
            res=res^num

        return res

        
        