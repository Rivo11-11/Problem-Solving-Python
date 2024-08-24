class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sum_square(n) :
            s = 0
            while n : 
                s += (n%10) ** 2
                n //=10
            return s
        myset = set()
        while True :
            if n == 1 : 
                return True
            if n not in myset :
                myset.add(n)
            else :
                return False
            n = sum_square(n)

        