class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0]) 
        def dfs(i,j) :
            if i == row or j == col or i  < 0 or j < 0 or grid[i][j] == '0' or grid[i][j] == '-1':
                return 
            
            ## mark as visited
            grid[i][j] = '-1'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        count = 0
        for i in range(row) :
            for j in range(col) :
                if grid[i][j] == '1' :
                    count += 1
                    dfs(i,j) 
        return count
        