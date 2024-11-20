class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        matrix = [[0 for i in range(n)] for j in range(n)]
        degree = defaultdict(int) 
        for u,v in roads : 
            matrix[u][v] = 1
            matrix[v][u] = 1
            degree[u] += 1 
            degree[v] += 1
        maxi = float('-inf')
        for i in range(n) :
            for j in range(i+1,n) :
                if i != j :

                    s = degree[i] + degree[j]
                    # if there is a connection subtract 1
                    if matrix[i][j] :
                        s -= 1
                    maxi = max(s,maxi)

        return maxi
            