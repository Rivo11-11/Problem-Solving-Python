class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0 :
            return False
        while n!= 1 :
            if n/4.0 != n // 4 :
                return False
            n /= 4
            
        return True