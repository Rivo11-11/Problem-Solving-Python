class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0 
        i = 0
        for c in reversed(s) :
            number += int(c) * 2**i
            i+=1
        step = 0
        while number != 1 :
            if number % 2 == 0 :
                number /= 2 
            else :
                number += 1
            step+=1
        return step
        