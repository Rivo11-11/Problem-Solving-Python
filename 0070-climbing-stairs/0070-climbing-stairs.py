class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        mymap = {}
        def rec(n) :
            if n in mymap :
                return mymap[n]
            if n == 0 :
                return 1 
            if n == -1 :
                return 0
            res = 0
            res += rec(n-1)
            res += rec(n-2)
            mymap[n] = res 
            return res
        return rec(n)