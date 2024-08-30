import copy
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        count_fresh  = 0
        rotten_image = []
        for i in range(row) :
            for j in range(col) :
                if grid[i][j] == 1 :
                    count_fresh +=1
                if grid[i][j] == 2 :
                    rotten_image.append((i,j))
        if count_fresh == 0 :
            return 0
        

        def bfs(grid,count_fresh,rotten_list) :
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            queue = deque(rotten_list)
            print(queue)
            minite = 0
            visited = set()
            for pair in rotten_list :
             visited.add(pair)
            while queue:

                for i in range(len(queue)):
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        new_x, new_y = x + dx, y + dy
                        
                        # Check if the new position is within bounds and not visited and not equal empty
                        if 0 <= new_x < row and 0 <= new_y < col and (new_x, new_y) not in visited and grid[new_x][new_y] != 0:
                                if grid[x][y] == 2 and grid[new_x][new_y] == 1 :
                                    grid[new_x][new_y] =  2 
                                    count_fresh -= 1
                                visited.add((new_x, new_y))
                                queue.append((new_x, new_y))
                minite +=1 
                if not count_fresh :
                    return minite
            return -1
        
        return bfs(grid,count_fresh,rotten_image)