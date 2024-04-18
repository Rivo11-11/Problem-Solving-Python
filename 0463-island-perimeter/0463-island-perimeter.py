class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        count = 0
        for i in range(r) :
            for j in range(c) :
                if grid[i][j] == 1 :
                    if j+1 >= c or grid[i][j + 1] != 1  :
                        count += 1
                    if j - 1 <= -1 or grid[i][j - 1] != 1:
                        count += 1 
                    if i - 1 <= -1 or grid[i - 1 ][j] != 1:
                        count += 1
                    if i + 1 >= r or grid[i + 1 ][j] != 1 :
                        count += 1 
        return count


        