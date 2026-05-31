class Solution:
    def reverseBits(self, n: int) -> int:
        return int('0b' + bin(n+2**32)[3:][::-1],2)