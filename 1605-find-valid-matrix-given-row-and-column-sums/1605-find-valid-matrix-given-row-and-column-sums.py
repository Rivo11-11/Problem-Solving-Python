class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        n = len(rowSum)
        m = len(colSum)
        res = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            res[i][0] = rowSum[i]
        # print(res)
        for j in range(m-1) :
            ## get the sum of this column 
            ## no need to loop on the last column will be already handled
            curr_col = 0
            for i in range(n) :
                curr_col += res[i][j]
            ## i need to adjust the need in a greedy way
            need = curr_col - colSum[j]
            for i in range(n) :
                mini = min(need,res[i][j]) 
                res[i][j+1] = mini
                res[i][j] -= mini
                need -= mini
        return res
                




        