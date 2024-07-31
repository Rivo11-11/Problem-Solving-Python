class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid) 
        col = len(obstacleGrid[0])
        ## memo for grid
        memo = [[-1 for _ in range(col)] for _ in range(row)]
        def dfs(i,j,row,col) :
            if j >= col or i >= row or obstacleGrid[i][j] == 1 :
                return 0
            if i == row - 1 and j == col -1  :
                return 1      
            if memo[i][j] != -1 :
                return memo[i][j]
            memo[i][j] = dfs(i,j+1,row,col) + dfs(i+1,j,row,col)
            return memo[i][j]
        return dfs(0,0,row,col)
 
            