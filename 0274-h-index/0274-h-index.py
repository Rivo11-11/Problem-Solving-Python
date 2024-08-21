class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        citations.sort()
        h = 0
        for i in range(n) :
           next_numbers  = n-i 
           if next_numbers <= citations[i] :
                h = max(next_numbers,h)
        return h
