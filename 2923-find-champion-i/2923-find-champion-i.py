class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ## grid[i][j] == 1 , i is stronger
        ## grid[i][i] = 0
        ##grid[i][j] != grid[j][i] 
        n = len(grid)
        id = 0
        for team in grid : 
            count_1 = 0
            for score in team :
                if score == 1 :
                    count_1 += 1 
                if count_1 == n-1 :
                    return id
            id +=1

                    