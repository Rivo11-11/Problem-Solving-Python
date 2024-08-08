class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        total = cols * rows 
        myset = set()
        res = []
        def dfs(i, j, direction):

                ## found an obstacle
                if i == rows or i < 0 or j == cols or j < 0 or (i, j) in myset:
                    return
                
                ## our base condition .all elements traversed
                if len(myset) == total:
                    return

                res.append(matrix[i][j])
                myset.add((i, j))

                # Define the order of directions: right, down, left, up
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                
                di, dj = directions[direction]
                ni, nj = i + di, j + dj

                ## continue to that direction if there is not obstacles
                if ni < rows and ni >= 0 and nj < cols and nj >= 0 and (ni, nj) not in myset:
                    dfs(ni, nj, direction)
                
                # Move to the next direction
                else:
                    dfs(i + directions[(direction + 1) % 4][0], j +     directions[(direction + 1) % 4][1], (direction + 1) % 4)

        dfs(0,0,0)
        return res
        