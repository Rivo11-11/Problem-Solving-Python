class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        myset = set()
        n = len(s)
        l,r = 0,0 
        maxi = float('-inf')
        rep = 0
        while r < n : 
            if r > 0 and s[r] == s[r-1] :
                myset.add(r-1)
                rep += 1
            while rep > 1 :
                if l in myset :
                    rep -= 1
                l+=1 
            maxi = max(maxi,r-l+1)
            r += 1
        return maxi
        

         