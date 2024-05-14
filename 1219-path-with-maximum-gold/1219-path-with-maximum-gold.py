class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid) 
        n = len(grid[0])
        myset = set()
        def dfs(i,j) :
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] == 0 or (i,j) in myset:
                return 0
            myset.add((i,j))
            current_gold = grid[i][j]
            max_neighbour = max(dfs(i,j+1) , dfs(i,j-1) ,  dfs(i+1,j) , dfs(i-1,j))
            myset.remove((i, j))
            return current_gold + max_neighbour
        maxi = 0
        for i in range(m) :
            for j in range(n) :
                if grid[i][j] != 0 :
                    maxi = max(dfs(i,j),maxi)
        return maxi

        