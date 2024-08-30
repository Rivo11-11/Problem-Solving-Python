class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        myset = set()
        n = len(stones)
        def dfs(i,j,k) :
            if k == n : 
                return
            for stone in stones :
                if (stone[0] == i or stone[1] == j)  and ((stone[0],stone[1]) not in myset) :
                    myset.add((stone[0],stone[1]))
                    dfs(stone[0],stone[1],k+1)  
                    

        clusters = 0
        for stone in stones :
            if (stone[0],stone[1]) not in myset :
                dfs(stone[0],stones[0],0) 
                clusters += 1
        return n - clusters