class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for i in range(n) :
            ## in - out
            graph[i+1] = [0,0]
        for u,v in trust :
            graph[u][1] += 1
            graph[v][0] += 1
        for node in graph :
            if graph[node][1] == 0 and graph[node][0] == n -1 :
                return node
        return -1 