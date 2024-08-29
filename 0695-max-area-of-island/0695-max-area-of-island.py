class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0]) 
        def dfs(i,j) :
            if i == row or j == col or i  < 0 or j < 0 or grid[i][j] == 0 or grid[i][j] == -1:
                return 0
            
            ## mark as visited
            grid[i][j] = -1
            return 1  + dfs(i+1,j) + dfs(i-1,j) +  dfs(i,j+1) + dfs(i,j-1)
        
        area = 0
        for i in range(row) :
            for j in range(col) :
                if grid[i][j] == 1 :

                   area = max(dfs(i,j),area)
        return area
        