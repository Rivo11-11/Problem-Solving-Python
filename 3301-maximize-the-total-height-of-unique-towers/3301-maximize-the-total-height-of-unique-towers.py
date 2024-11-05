class Solution(object):
    def maximumTotalSum(self, maximumHeight):
        """
        :type maximumHeight: List[int]
        :rtype: int
        """
        maximumHeight.sort()
        n = len(maximumHeight)
        ans = maximumHeight[n-1]
        for i in range(n-2,-1,-1) :
            if maximumHeight[i] >= maximumHeight[i+1] :
                maximumHeight[i] = maximumHeight[i+1] - 1
                if maximumHeight[i] <= 0 :
                    return -1
            ans += maximumHeight[i]
        return ans