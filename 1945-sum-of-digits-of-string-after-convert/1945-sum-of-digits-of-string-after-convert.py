class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ## 96 our special number .. ord(a) - 96 = 1
        temp = ''
        for i in range(len(s)) :
            temp += str(ord(s[i])-96)
        
        s = 0
        while k :
            s = 0
            for i in range(len(temp)) :
                s += int(temp[i])
            temp = str(s)
            k-=1

        return s

        