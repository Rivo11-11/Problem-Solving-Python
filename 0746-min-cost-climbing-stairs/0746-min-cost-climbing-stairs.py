class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        size = len(cost)
        mymap = {}
        def func(n) :
            if n <= 1 : 
                return cost[n]
            if n in mymap :
                return mymap[n]
            s = cost[n] if n < size else 0
            s += min(func(n-1),func(n-2))
            mymap[n] = s 
            return s
        return func(size)
        