class Solution:
    def numDecodings(self, s: str) -> int:
        # pattern: fib + conditions
        dp = [0] * (len(s) + 1) # 1 indexed
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1 # we indexed right here.

        for i in range(2, len(s) + 1):
            two_digit = int(s[i-2:i]) # convert string to integer
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[len(s)]