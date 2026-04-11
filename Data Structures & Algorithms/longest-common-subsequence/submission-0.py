class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        cache = [0] * (len(text2)+1)
        for i in range(len(text1)-1 , -1, -1):
            prev = 0
            for j in range(len(text2)-1 , -1, -1):
                temp = cache[j]
                if text1[i] == text2[j]:
                    cache[j] = 1 + prev
                else:
                    cache[j] = max(cache[j], cache[j+1])
                prev = temp
        return cache[0]