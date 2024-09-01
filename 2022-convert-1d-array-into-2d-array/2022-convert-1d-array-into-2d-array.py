class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        length = len(original)
        k = 0
        res = []
        if m*n != length :
            return []
        for  i in range(m) :
            temp = []
            for j in range(n) :
                    temp.append(original[k]) 
                    k+=1
            res.append(temp[:])
        return res

         