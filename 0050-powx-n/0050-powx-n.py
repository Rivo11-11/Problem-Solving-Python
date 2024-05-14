class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # def power(x,n) :
        #     if n == 0 : return 1 
        #     if n < 0 :
        #         return 1.0 / x * power(x,n+1)
        #     return x * power(x,n-1)
        # return power(x,n)
        def power(x, n):
            if n == 0:
                return 1
            if n < 0:
                x = 1 / x
                n = -n
            result = 1
            while n > 0:
                if n % 2 == 1:
                    result *= x
                x *= x
                n //= 2
            return result
        return power(x,n)
        
        