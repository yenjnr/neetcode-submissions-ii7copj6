class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def f(si, pi):
            if pi == len(p):
                return si == len(s)

            if (pi, si) in cache:
                return cache[(pi, si)]
            
            result = False
            pstar = pi+1 < len(p) and p[pi+1] == '*'
            if si < len(s):
                if not pstar:
                    if p[pi] == '.' or p[pi] == s[si]:
                        result = f(si+1, pi+1)                
                elif p[pi] != '.' and p[pi] != s[si]:
                    result = f(si, pi+2)
                else:
                    result = f(si, pi+2) or f(si+1, pi)
            elif pstar:
                result = f(si, pi+2)
            cache[(pi,si)] = result
            return result
        return f(0, 0)