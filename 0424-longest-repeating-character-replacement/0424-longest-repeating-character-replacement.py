class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        mymap = {} 
        n = len(s) 
        l,r = 0,0 
        maxi = 0
        while r < n : 
            if s[r] not in mymap :
                mymap[s[r]] = 1 
            else : 
                mymap[s[r]] += 1 

            while r-l+1 - max(mymap.values()) > k : 
                mymap[s[l]] -= 1
                l+=1
            maxi = max(maxi,r-l+1)
            r+=1 
        return maxi

            
        