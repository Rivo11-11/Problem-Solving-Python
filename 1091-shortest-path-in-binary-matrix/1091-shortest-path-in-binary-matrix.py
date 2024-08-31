class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        queue = deque([(0,0)])
        myset = set((0,0))
        self.count = 1
        self.flag = False
        def bfs() : 
                while queue :
                    for i in range(len(queue)) :
                        ## 8 directions
                        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
                        x,y = queue.popleft()
                        # print(x,y)
                        if x == row -1 and y == col - 1 :
                                self.flag = True
                                return self.count
                        for dx,dy in directions :
                            new_x = x + dx
                            new_y = y + dy
                            if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] != 1 and (new_x,new_y) not in myset :
                                if new_x == row-1 and new_y == col -1 :
                                    self.flag = True
                                queue.append((new_x,new_y))
                                myset.add((new_x,new_y))
    

                    self.count+=1
                    if self.flag :
                        return self.count   

        if grid[0][0] == 1 :
                return -1      
        ans  = bfs()
        if not self.flag :
            return -1
        return ans
        


        