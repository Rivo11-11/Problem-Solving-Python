class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        ## [6,1,5,10,3]
        n = len(values) 
        l,r = 0,1
        maxi = 0 
        while r < n :
            maxi = max(maxi,values[l] + values[r] - (r-l)) 
            if values[r] + (r-l) >= values[l] :
                l = r 
            r+=1 
        return maxi 

