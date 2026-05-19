class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        st_x = str(x)
        if x <0:
            sign = -1
            st_x = st_x[1:]

        
        max_int = pow(2,31)+1
        #print(max_int)
        no = 0
        multiplier = 1
        for i in range(len(st_x)):
            no += (multiplier * int(st_x[i]))
            multiplier = multiplier * 10
            if no > max_int:
                return 0

        return sign * no