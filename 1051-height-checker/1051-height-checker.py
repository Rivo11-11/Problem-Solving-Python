class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        temp = heights[:]
        heights.sort()
        count = 0
        for i in range(n) :
            if heights[i] != temp[i] :
                count+=1
        return count