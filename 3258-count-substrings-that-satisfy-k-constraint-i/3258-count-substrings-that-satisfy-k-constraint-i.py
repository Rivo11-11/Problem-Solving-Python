class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s) 
        l,r = 0,0 
        mymap = {'1' : 0 , '0' : 0}
        count = 0
        while r < n  : 
            mymap[s[r]] +=1
            while mymap['0'] > k and mymap['1'] > k :
                mymap[s[l]] -= 1 
                l +=1
            count += r-l+1
            r +=1
        return count
