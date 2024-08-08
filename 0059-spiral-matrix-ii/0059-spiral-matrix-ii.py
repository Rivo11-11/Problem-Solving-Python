class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rows = n 
        cols = n 
        matrix = [[0] * n for _ in range(n)]
        total = rows * cols 
        myset = set()
        res = []
        def dfs(i, j, direction,num):
                if i == rows or i < 0 or j == cols or j < 0 or (i, j) in myset:
                    return
                
                if len(myset) == total:
                    return

                matrix[i][j] = num
                myset.add((i, j))


                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                
                di, dj = directions[direction]
                ni, nj = i + di, j + dj

                ## continue to that direction if there is not obstacles
                if ni < rows and ni >= 0 and nj < cols and nj >= 0 and (ni, nj) not in myset:
                    dfs(ni, nj, direction,num+1)
                
                # Move to the next direction
                else:
                    dfs(i + directions[(direction + 1) % 4][0], j +     directions[(direction + 1) % 4][1], (direction + 1) % 4,num+1)

        dfs(0,0,0,1)
        return matrix
        
        