class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.target = '0'
        def invert(arr) :
            temp = ''
            for i in range(len(arr)) :
                if arr[i] == '1' :
                    temp += '0'
                else :
                    temp += '1'
            return temp
        def rec(stop) :
            if stop == n :
                return 
            temp = self.target[:]
            self.target += "1"
            temp2 = invert(temp) 
            self.target += temp2[::-1] 
            rec(stop+1)
        rec(1)
        return self.target[k-1]