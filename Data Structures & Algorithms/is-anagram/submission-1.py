class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = "".join(sorted(s))
        t1 = "".join(sorted(t))
        for i in range(len(s)):
            if t1[i] != s1[i]:
                return False 
        return True
                

                
            

