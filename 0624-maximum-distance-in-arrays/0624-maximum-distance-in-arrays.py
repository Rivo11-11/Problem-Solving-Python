class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        max_dist = float('-inf')
        mini = arrays[0][0]
        maxi = arrays[0][-1]
        n = len(arrays)
        for i in range(1,n) :
            max_dist = max(max_dist,maxi - arrays[i][0],arrays[i][-1]-mini)
            mini = min(mini,arrays[i][0]) 
            maxi = max(maxi,arrays[i][-1])
        return max_dist