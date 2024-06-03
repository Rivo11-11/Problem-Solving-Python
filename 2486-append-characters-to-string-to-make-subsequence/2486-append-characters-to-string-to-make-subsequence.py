class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n1 = len(s) 
        n2 = len(t) 
        s1 = 0 
        t1 = 0
        while s1 < n1 and t1 < n2 :
            if s[s1] == t[t1] :
                s1 += 1 
                t1 += 1
            else : s1 += 1
        if t1 == n2 :
            return 0
        return n2 - t1 

        