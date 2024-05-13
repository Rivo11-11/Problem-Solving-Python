class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(m) :
            ## if MSB is 0 turn the flag on
            flag = False
            if grid[i][0] == 0 :
                grid[i][0] = 1
                flag = True
            if flag :
                for j in range(1,n) :
                    grid[i][j] = 1 if grid[i][j] == 0 else 0
        mymap = {}
        for j in range(n) :
            count_0 = 0
            for i in range(m) :
                if grid[i][j] == 0 :
                    count_0 += 1
            mymap[j] = True if count_0 > m // 2 else False
        for j in range(n) :
            if mymap[j] :
                for i in range(m) :
                    grid[i][j] = 1 if grid[i][j] == 0 else 0
        res = 0
        for i in range(m) :
            k = 1
            for j in range(n) :
                if grid[i][j] == 1 :
                    res += 2**(n-k)
                k+=1
        return res

                
        