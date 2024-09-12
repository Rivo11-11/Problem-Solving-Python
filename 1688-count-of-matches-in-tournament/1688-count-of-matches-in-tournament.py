class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 1:
            temp = n
            count += n // 2
            n //= 2
            if temp % 2 == 1 :
                n+=1    
        return count


