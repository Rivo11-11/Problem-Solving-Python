class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ## trick is to use a priority queue over a heap queue.
        queue = [(0, 0, 0)]  # (cost, x, y)
        row = len(grid)
        col = len(grid[0])
        mymap = defaultdict(lambda: float('inf'))
        mymap[(0,0)] = 0
        vector = [(0,1), (1,0), (0,-1), (-1,0)]
        
        while queue:
            cost, x, y = heapq.heappop(queue)
            if x == row - 1 and y == col - 1:
                return cost
            for dx, dy in vector:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < row and 0 <= new_y < col:
                    new_cost = cost + grid[new_x][new_y]
                    if new_cost < mymap[(new_x, new_y)]:
                        mymap[(new_x, new_y)] = new_cost
                        heapq.heappush(queue, (new_cost, new_x, new_y))
    

        