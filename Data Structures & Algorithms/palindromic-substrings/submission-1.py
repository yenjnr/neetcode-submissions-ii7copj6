class Solution:
    def countSubstrings(self, s: str) -> int:
        # same palindromic idea
        # but this time, we count every occurance
        n = len(s)
        
        if n == 1:
            return 1

        count = 0

        # odd length substrings
        for i in range(n):
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
        
        # even length substrings
        for i in range(n - 1):
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1

        return count
        
        
        

