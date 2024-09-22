class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected[0])
        visited = set()

        def dfs(i) :
            
            if i in visited :
                return False
            
            visited.add(i)
            for j in range(n) :
                if i != j and  isConnected[i][j] == 1 :
                   dfs(j)
            
            return True

        count = 0
        for i in range(n) :
            if dfs(i) :
                count += 1
        return count