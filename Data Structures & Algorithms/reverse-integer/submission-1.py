class Solution:
    def reverse(self, x: int) -> int:

        string=str(x)
        
        if string[0]=="-":
            string=string[1:]
            string=string[::-1]
            number=-int(string)
        else:
            string=string[::-1]
            number=int(string)

        if abs(number) > 2**31-1:
            return 0

        return number