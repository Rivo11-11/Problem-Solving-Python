class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        s = sum(chalk)
        k = k % s  
        n = len(chalk)
        for i in range(n):
            if chalk[i] > k:
                return i
            k -= chalk[i]
        return 0
