class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))) :
            digits[i] += 1 
            if digits[i] == 10 :
                digits[i] = 0
            else :
                break
        if digits[0] == 0 :
            digits = [1] + digits
        return digits
        