class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        def rec(columnTitle,n,index,cumm) :
            if index == n :
                return cumm
            new = ord(columnTitle[index]) - 64
            return rec(columnTitle,n,index+1,cumm * 26 + new)
        n = len(columnTitle) 
        return rec(columnTitle,n,0,0)

        