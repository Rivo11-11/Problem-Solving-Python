class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        maxi = []
        maxi.append(0)
        mymap = {}
        def dfs(i,j,prev) :
            if i >= m or i < 0 or j >= n or j < 0 or matrix[i][j] <= prev :
                return 0
            if (i,j) in mymap :
                return mymap[(i,j)]
            res = 1 
            res = max(res,1+ dfs(i,j+1,matrix[i][j]))
            res = max(res,1+ dfs(i,j-1,matrix[i][j]))
            res = max(res,1+ dfs(i+1,j,matrix[i][j]))
            res = max(res,1+ dfs(i-1,j,matrix[i][j]))
            maxi[0] = max(res,maxi[0])
            mymap[(i,j)] = res
            return res

        for i in range(m) :
            for j in range(n) :
                dfs(i,j,-1)
        return maxi[0]

        